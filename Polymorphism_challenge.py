class Vehicle:
    """
    Base class for vehicles.
    """
    def move(self):
        """
        Base method to define movement (to be overridden).
        """
        return "This vehicle moves in a unique way."

class Car(Vehicle):
    """
    Represents a car.
    """
    def move(self):
        return "The car is driving on the road. 🚗"

class Plane(Vehicle):
    """
    Represents an airplane.
    """
    def move(self):
        return "The plane is flying in the sky. ✈️"

class Boat(Vehicle):
    """
    Represents a boat.
    """
    def move(self):
        return "The boat is sailing on the water. 🚤"


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
