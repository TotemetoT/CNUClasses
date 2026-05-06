# ChatGPT helped me generate this simple example of using a dictionary with class definitions.
# Prompt: write me a short simple demo of python class,
#         creating a dictionary of class name to class definition,
#         then using dictionary to look up defintion and create instance
#
# Reply: Here is a simple Python demo that demonstrates how to create a dictionary mapping class names to class definitions,
#        and then use that dictionary to look up a class definition and
#        create an instance of the class:
#        In this demo:
#            We define two simple classes, Dog and Cat, each with a method speak().
#            We create a dictionary class_dict that maps the class names ("Dog", "Cat")
#            to their corresponding class definitions.
#            The create_instance() function looks up the class name in the dictionary
#            and creates an instance of the class with the provided arguments.

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"

# Create a dictionary mapping class names (as strings) to class definitions
class_dict = {
    "Dog": Dog,
    "Cat": Cat
}

# Function to create an instance using the class dictionary
def create_instance(class_name, *args):
    if class_name in class_dict:
        return class_dict[class_name](*args)  # Here is the magic to construct instance
    else:
        raise ValueError(f"Class {class_name} not found in class_dict.")

# Example usage
pet = create_instance("Dog", "Buddy")
print(pet.speak())  # Output: Buddy says Woof!

pet = create_instance("Cat", "Whiskers")
print(pet.speak())  # Output: Whiskers says Meow!
