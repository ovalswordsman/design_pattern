from abc import ABC, abstractmethod


# Creator Interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass