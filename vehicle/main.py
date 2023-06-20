from car_factory import CarFactory
from motorcycle_factory import MotorcycleFactory
from truck_factory import TruckFactory


if __name__ == "__main__":
    # User's input
    vehicle_type = input("Enter the type of vehicle you want to manufacture (car, motorcycle, or truck): ")

    # Vehicle creation based on user's input
    if vehicle_type.lower() == "car":
        factory = CarFactory()
    elif vehicle_type.lower() == "motorcycle":
        factory = MotorcycleFactory()
    elif vehicle_type.lower() == "truck":
        factory = TruckFactory()
    else:
        print("Invalid vehicle type.")
        exit()

    # Manufacturing the vehicle
    vehicle = factory.create_vehicle()

    # Display vehicle details
    vehicle.display_details()