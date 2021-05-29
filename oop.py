class Person:

    class_property = "This is Class Property"

    def __init__(self, name: str = None):
        self.message = "Behave like a constructor"
        self.name = name

    def public_method(self, integer_input: int) -> str:
        return "Integer Input: " + str(integer_input)

    def _private_method(self):
        return "This is Private Method"


# Instantiate the Person Class
person_instance = Person()

# Call Person instance public method with parameter
output_of_public_method = person_instance.public_method(120)

# Print the output of the method
print(output_of_public_method)

# Print the class property
print(person_instance.class_property)


# Instantiate the Person Class with parameter
person_instance = Person("Mia")

# Print the constructor initiate property
print(person_instance.name)


class Student(Person):

    def some_method(self):
        return "Some Method"
