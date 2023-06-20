from vehicle import Vehicle


# Concrete Product
class Motorcycle(Vehicle):
    def display_details(self):
        print("Motorcycle: 2 wheels, 2 seating capacity, maximum speed 180 km/h")