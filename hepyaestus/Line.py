from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Callable, Optional

from hepyaestus.EventData import EventData
from hepyaestus.Store import StoreNode

if TYPE_CHECKING:
    from hepyaestus.Base import BaseObject
    from hepyaestus.Entity import Entity
    from hepyaestus.Exit import Exit
    from hepyaestus.Machine import Machine
    from hepyaestus.Queue import Queue
    from hepyaestus.Source import Source
    from simpy import Environment


class Line:
    def __init__(
        self,
        objectList: list,
        routingPriority: Optional[Callable[[StoreNode], int]] = None,
    ) -> None:
        self.ObjList: list[StoreNode] = [
            object for object in objectList if isinstance(object, StoreNode)
        ]

        sortByClass: dict[str, list] = defaultdict(list)
        for object in objectList:
            sortByClass[object.__class__.__name__].append(object)

        self.ExitList: list[Exit] = sortByClass['Exit']
        self.MachineList: list[Machine] = sortByClass['Machine']
        self.QueueList: list[Queue] = sortByClass['Queue']
        self.SourceList: list[Source] = sortByClass['Source']
        self.EntityList: list[Entity] = sortByClass['Entity']

        self.routingPriority: Optional[Callable[[StoreNode], int]] = routingPriority

        self.settings: dict[str, bool | None | list[BaseObject]] = {
            'traceIsOn': True,  # checked by baseObject before calling printTrace
            'printFiltering': None,  # print only those in list if not None
        }

    def initialize(self, env: Environment) -> None:
        self.env = env
        for object in self.ObjList:
            object.initialize(self.env, self)
            self.env.process(object.run())
        self.setWorkInProgress()

    def setWorkInProgress(self) -> None:
        if self.EntityList is None:
            return

        stationsWithWIP: set[StoreNode] = set()

        self.EntityList.reverse()  # to maintain order: (LIFO)
        for entity in self.EntityList:
            assert entity.startingStation is not None, (
                'Entity created for Work in Progress must have startingStataion'
            )
            stationsWithWIP.add(entity.startingStation)
            entity.initialize(self.env, self, currentStation=entity.startingStation)
            entity.startingStation._receive(entity=entity)

        for station in stationsWithWIP:
            station.initialWIP.succeed(EventData(caller=station, time=self.env.now))

    def turnTraceingOff(self) -> None:
        self.settings['traceIsOn'] = False

    def canTrace(self, object: BaseObject) -> bool:
        if not self.settings['traceIsOn']:
            return False
        if self.settings['printFiltering'] is not None:
            assert type(self.settings['printFiltering']) is list
            return object in self.settings['printFiltering']
        return True

    def filterTrace(self, filter: BaseObject) -> None:
        if self.settings['printFiltering'] is None:
            self.settings['printFiltering'] = [filter]
        else:
            assert type(self.settings['printFiltering']) is list
            self.settings['printFiltering'].append(filter)
