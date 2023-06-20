from vehicle import Vehicle


# Concrete Product
class Car(Vehicle):
    def display_details(self):
        print("Car: 4 wheels, 5 seating capacity, maximum speed 200 km/h")