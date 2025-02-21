from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hepyaestus.baseClasses import BaseObject, CoreObject
    from simpy import Environment

    # from hepyaestus.Exit import Exit
    # from hepyaestus.Machine import Machine
    # from hepyaestus.Queue import Queue
    # from hepyaestus.Source import Source


class Line:
    def __init__(self, objectList: list) -> None:
        self.ObjList: list[CoreObject] = objectList

        # self.ExitList: list[Exit] = [objectList[3]]
        # self.MachineList: list[Machine] = [objectList[2]]
        # self.QueueList: list[Queue] = [objectList[1]]
        # self.SourceList: list[Source] = [objectList[0]]

        self.settings: dict[str, bool | None | list[BaseObject]] = {
            'traceIsOn': True,  # checked by baseObject before calling printTrace
            'printFiltering': None,  # print only those in list if not None
        }

    def initialize(self, env: Environment) -> None:
        self.env = env
        for object in self.ObjList:
            object.initialize(self.env, self)
            self.env.process(object.run())

    def turnTraceingOff(self) -> None:
        self.settings['traceIsOn'] = False

    def canTrace(self, object: BaseObject) -> bool:
        if not self.settings['traceIsOn']:
            return False
        if self.settings['printFiltering'] is not None:
            assert type(self.settings['printFiltering']) is list
            return object in self.settings['printFiltering']
        return True

    def filterTrace(self, filter: BaseObject):
        if self.settings['printFiltering'] is None:
            self.settings['printFiltering'] = [filter]
        else:
            assert type(self.settings['printFiltering']) is list
            self.settings['printFiltering'].append(filter)
