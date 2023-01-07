
class Math:
    """ A global class"""
    @staticmethod
    def add5(x):
        """ A static method"""
        return x + 5




class Pet:
    """ This class represents a Pet object"""
    number_of_pets = 0  # class attribute number
    ASTATICVAR = 98.6  # A static class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.add_number_of_pets()
    @classmethod
    def number_of_pets_(cls):
        """class attribute number """
        return cls.number_of_pets
    @classmethod
    def add_number_of_pets(cls):
        """ class attribute number """
        cls.number_of_pets += 1
    @classmethod
    def print_number_of_pets(cls):
        """ class attribute number """
        print(cls.number_of_pets)    
    def show(self):
        """A function to display the attributes if this class"""
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    """This is a class of type Cat"""
    def __init__(self, name, age, breed):  # Note that this class has a different constructor
        super().__init__(name, age)         # super CALLS the prior constructor from the upper class
        self.breed = breed
    def show(self):
        """A function to display the attributes if this class"""
        print(f"I am {self.name} and I am {self.age} years old, and I am a breed of {self.breed}")
    def speak(self):
        """This method prints the sounds of this class"""
        print("Meow meow")
class Dog(Pet):
    """This is a class of type Dog"""
    def speak(self):
        """ No __init___ needed"""
        """This method prints the sounds of this class"""
        print("Ruff ruff")
p = Pet("Bill", 12)
p.show()
d = Dog("Prince",3 )
d.show()

c = Cat("Kitty", 2)
c.show()

c.speak()
d.speak()





