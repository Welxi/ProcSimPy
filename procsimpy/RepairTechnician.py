from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.Resource import ResourceObject

if TYPE_CHECKING:
    from procsimpy.Failure import Failure
    from simpy.resources.resource import Request


class RepairTechnician(ResourceObject):
    def __init__(self, id: str, name: str, *, capacity: int = 1) -> None:
        super().__init__(id, name, capacity=capacity)
        self.failures = None

    def filterFailures(self, failures: list[Failure]) -> None:
        self.failures = failures

    def request(self, cause) -> Request:  # type: ignore
        if self.failures is not None and cause not in self.failures:
            raise ValueError('Cause not in Failures that can be resolved')
        return super().request()
