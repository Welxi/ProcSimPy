from procsimpy.Resource import ResourceObject


class RepairTechnician(ResourceObject):
    def __init__(self, id: str, name: str, *, capacity: int = 1) -> None:
        super().__init__(id, name, capacity=capacity)
