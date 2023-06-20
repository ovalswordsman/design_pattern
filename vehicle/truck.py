from vehicle import Vehicle


# Concrete Product
class Truck(Vehicle):
    def display_details(self):
        print("Truck: 6 wheels, 3 seating capacity, maximum speed 160 km/h")