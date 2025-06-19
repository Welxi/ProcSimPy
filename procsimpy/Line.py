from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Callable, Optional

if TYPE_CHECKING:
    from procsimpy.AvailabilityToken import AvailabilityToken
    from procsimpy.Base import Base
    from procsimpy.Entity import Entity
    from procsimpy.Exit import Exit
    from procsimpy.Failure import Failure
    from procsimpy.Node import Node
    from procsimpy.Queue import Queue
    from procsimpy.RepairTechnician import RepairTechnician
    from procsimpy.Server import Server
    from procsimpy.Source import Source
    from simpy import Environment
    from simpy.resources.resource import Request


# ? how do we handle scrapping entities, i think entities should tell line
#  they are scraped and line creates a scrap store to hold them and adds to node list


class Line:
    """
    Orchestration Module for Nodes, controlles logging/printing behaviour
    and initializeing components at the start of Experiment Iterations
    any Knowledge that nodes require of system not in their neighbours should be provided here
    """

    def __init__(
        self,
        nodeList: list[Node],
        *,
        WIPList: Optional[list[Entity]] = None,
        failures: Optional[list[Failure]] = None,
        repair: Optional[
            list[RepairTechnician]
        ] = None,  # can change to resources when operators is available
        routingPriority: Optional[
            Callable[[list[AvailabilityToken]], AvailabilityToken]
        ] = None,
    ) -> None:
        if WIPList is None:
            WIPList = []
        self.nodeList = nodeList
        self.WIPList = WIPList

        sortByClass: dict[str, list] = defaultdict(list)
        for node in self.nodeList:
            sortByClass[node.__class__.__name__].append(node)

        # TODO change this list to accept inheritors of these classes
        self.ExitList: list[Exit] = sortByClass['Exit']
        self.ServerList: list[Server] = sortByClass['Server']
        self.QueueList: list[Queue] = sortByClass['Queue']
        self.SourceList: list[Source] = sortByClass['Source']

        if bool(failures) != bool(repair):
            raise ValueError(
                'failures and repair either both need to be set or both need to be None'
            )
            # ? is this true maybe an experiment wants no resloution to failures
            # turn to warning instead
            # maybe a double warning if a long running experiment- start and end
            # skipped a lot of time do to no action because of failures stoping loops

        self.FailureList: list[Failure] = failures if failures else []

        # ? Could just make this automatic
        # would need to remove the ability to filter what failures are resolved
        self.RepairTechList: list[RepairTechnician] = repair if repair else []
        if len(self.RepairTechList) > 1:
            raise NotImplementedError(
                'While in beta only one Repair Technician is supported'
            )

        self.routingPriority: Optional[
            Callable[[list[AvailabilityToken]], AvailabilityToken]
        ] = routingPriority

        self.settings: dict[str, bool | None | list[Node]] = {
            'traceIsOn': True,  # checked by baseObject before calling printTrace
            'printFiltering': None,  # print only those in list if not None
        }

    def initialize(self, env: Environment) -> None:
        self.env = env

        # TODO Check for circular Routing
        # And Advance Below to check whole node chain
        # self.giver: Self | None = self.previous[0] if self.previous else None
        # self.receiver: Self | None = self.next[0] if self.next else None

        # if self.giver is not None:
        #     assert self.giver.giver is not self, 'Circular Process Chain'
        # if self.receiver is not None:
        #     assert self.receiver.receiver is not self, 'Circular Process Chain'

        for node in self.nodeList:
            node.initialize(env=self.env, line=self)

        for failure in self.FailureList:
            failure.initialize(env=self.env, line=self)

        for repair in self.RepairTechList:
            repair.initialize(env=self.env, line=self)

        for entity in self.WIPList:
            assert entity.startingNode is not None
            entity.initialize(env=self.env, line=self, currentNode=entity.startingNode)

        self.setWorkInProgress()

    def setWorkInProgress(self) -> None:
        for entity in self.WIPList:
            assert entity.startingNode is not None, (
                'Entity created for Work in Progress must have startingNode'
            )
            entity.startingNode.put(entity)

    def turnTraceingOff(self) -> None:
        self.settings['traceIsOn'] = False

    def canTrace(self, base: Base) -> bool:
        if not self.settings['traceIsOn']:
            return False
        if self.settings['printFiltering'] is not None:
            assert type(self.settings['printFiltering']) is list
            return base in self.settings['printFiltering']
        return True

    def filterTrace(self, node: Node) -> None:
        if self.settings['printFiltering'] is None:
            self.settings['printFiltering'] = [node]
        else:
            assert type(self.settings['printFiltering']) is list
            self.settings['printFiltering'].append(node)

    def partsCreated(self) -> int:
        return sum(exit.stats.numberOfEntitiesEntered for exit in self.ExitList)

    def repairRequest(self, cause) -> Request:
        if not self.RepairTechList:
            raise ValueError('No repair Tech available')

        # TODO Handle many repair techs
        # easyest way is to just make the Resource have a higher capacity
        # would need to model skills / fixable failuremodes for any more complexity to matter
        return self.RepairTechList[0].request(cause)
