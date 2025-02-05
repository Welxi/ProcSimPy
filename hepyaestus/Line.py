from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hepyaestus.baseClasses import CoreObject
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

        self.traceIsOn = True

    def initialize(self, env: Environment) -> None:
        self.env = env
        for object in self.ObjList:
            object.initialize(self.env, self)
            self.env.process(object.run())

    def turnTraceingOff(self):
        self.traceIsOn = False
