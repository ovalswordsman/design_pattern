from vehicle_factory import VehicleFactory
from truck import Truck


# Concrete Creator
class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()