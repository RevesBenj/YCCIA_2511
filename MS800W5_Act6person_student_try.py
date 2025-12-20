# Base class Person
class Person:
    def __init__(self, name, address, age):
        # Store common information for all persons
        self._name = name #protected access, Accessible inside the class and child classes
        # self.__name = name
        self.address = address
        self.age = age

    def greet(self):
        # Default greeting method for Person
        print("Greetings and felicitations from the maestro " + self.name)


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, address, age, student_id):
        # Call the parent (Person) constructor to reuse code
        super().__init__(name, address, age)

        # Store student-specific information
        self.student_id = student_id

    def greet(self):
        # This method overrides the greet() method in Person
        # Same method name, but different output
        # print("Hi " + self.__name)
        print("Hi " + self._name) # Accessible inside the class and child classes


# Create a Student object
student1 = Student("Alice", "123 Main St", 20, "S12345")

# Call greet() on the Student object
student1.greet()
