from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from hepyaestus.Interruption import Interruption
from hepyaestus.RandomNumberGenerator import RandomNumberGenerator

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.ProbDistribution import ProbDistribution
    from hepyaestus.RepairTechnician import RepairTechnician
    from hepyaestus.StoreNode import StoreNode


class Failure(Interruption):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        victim: StoreNode,
        TTF: ProbDistribution,
        TTR: ProbDistribution,
        repair: Optional[RepairTechnician] = None,
    ) -> None:
        super().__init__(id, name, victim=victim)
        self.TTF = RandomNumberGenerator(TTF)
        self.TTR = RandomNumberGenerator(TTR)
        self.repair = repair

    def run(self) -> Generator:
        while True:
            yield self.env.timeout(self.TTF.generateNumber())

            self.interrupt()

            if self.repair:
                with self.repair.request() as repairTech:
                    yield repairTech

                    yield self.env.timeout(self.TTR.generateNumber())

                    self.reactivate()
