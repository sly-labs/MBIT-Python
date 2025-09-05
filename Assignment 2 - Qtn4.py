# Define the Dog class with make_sound method
class Dog:
    def make_sound(self):
        return "Woof! Woof!"

# Define the Cat class with make_sound method
class Cat:
    def make_sound(self):
        return "Meow! Meow!"

# The function that works with any object that has a make_sound() method
def process_sound(sound_object):
    # Doesn't care about the type — just calls make_sound()
    print(f"Sound: {sound_object.make_sound()}")

# Example usage
dog = Dog()
cat = Cat()

# Same function works with both types
process_sound(dog)  # Output: Sound: Woof! Woof!
process_sound(cat)  # Output: Sound: Meow! Meow!

"""
Key Points:
Duck Typing: Python uses duck typing — "if it walks like a duck and quacks like a duck, it's a duck." If an object has a make_sound() method, it can be used by process_sound().
No Inheritance Required: The Dog and Cat classes don't need to inherit from a common base class (though they could). They just need to implement the expected interface.
Polymorphic Behavior: The process_sound() function is polymorphic — it can handle different types uniformly.
"""