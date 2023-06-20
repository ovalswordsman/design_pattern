from vehicle_factory import VehicleFactory
from motorcycle import Motorcycle


# Concrete Creator
class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()