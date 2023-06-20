from vehicle_factory import VehicleFactory
from car import Car


# Concrete Creator
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()