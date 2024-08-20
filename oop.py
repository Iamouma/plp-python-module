class Person:
    def __init__(self, name, age, gender):
        """Initialize the Person object with name, age, and gender."""
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        """Prints an introduction message with the person's details."""
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")
        
# Create an instance of the Person class
person = Person("Mwabili", 35, "Male")

# Call the introduce method to display the person's information
person.introduce()
