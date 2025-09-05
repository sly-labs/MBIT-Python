# This is a simple class hierarchy demonstrating inheritance and method overriding:
# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        """Base method that can be overridden by subclasses"""
        return f"The {self.year} {self.brand} {self.model} engine is starting..."

    def get_info(self):
        """Method to display vehicle information"""
        return f"{self.year} {self.brand} {self.model}"


# Subclass Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors=4):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        """Override the base method for Car"""
        return f"The {self.year} {self.brand} {self.model} car engine roars to life with a VROOM!"

    def honk(self):
        """Car-specific method"""
        return "Beep beep!"


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type="motorcycle"):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def start_engine(self):
        """Override the base method for Bike"""
        return f"The {self.year} {self.brand} {self.model} bike engine starts with a ZOOM!"

    def wheelie(self):
        """Bike-specific method"""
        return "Popping a wheelie!"


# Example usage
if __name__ == "__main__":
    # Create instances
    car = Car("Toyota", "Camry", 2023, 4)
    bike = Bike("Harley-Davidson", "Street 750", 2022, "cruiser")

    # Demonstrate method overriding
    print(car.get_info())
    print(car.start_engine())  # Uses overridden method in Car
    print(car.honk())

    print("\n" + bike.get_info())
    print(bike.start_engine())  # Uses overridden method in Bike
    print(bike.wheelie())

    # Show polymorphism - same method name, different behavior
    print("\n--- Polymorphism demonstration ---")
    vehicles = [car, bike]
    for vehicle in vehicles:
        print(vehicle.start_engine())
"""
Key Concepts Demonstrated:
Inheritance: Both Car and Bike inherit from the Vehicle base class using class Car(Vehicle):
Method Overriding: The start_engine() method is defined in the base class and overridden in both subclasses to provide vehicle-specific behavior.
Super(): Used in subclasses to call the parent class constructor while adding additional parameters.
Polymorphism: The same method name (start_engine()) behaves differently depending on the object type.
Encapsulation: Each class has its own attributes and methods, with some being specific to that vehicle type.
This hierarchy shows how the base class provides common functionality while subclasses can customize behavior through method overriding.
"""