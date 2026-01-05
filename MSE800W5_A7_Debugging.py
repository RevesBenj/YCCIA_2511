
# -------------------------------------------------------
# Week 5 - Activity 7 Debugging
# Author: Benjelyn Reves Patiag
# Date Created: 5-Jan-2026
# Description: Run the attached code and explain what is there error if there is any and how we can solve it.
# -------------------------------------------------------

"""
Error Explanation:
Variable start with double underscore like __age, Python change the name automatic so people cannot access or override easy in child class.
So inside Person, when you write self.__age, Python actually save it as:
self._Person__age
Because of that, s1.__age is not exist in the object, so Python throw AttributeError.
The correct and proper way is what you already do, using:
s1.get_age()
"""



class Person:
    def __init__(self, name, address, age):
        # Public attribute: can access anywhere, no problem
        self.name = name

        # Protected by rule only, still can access but should not outside
        self._address = address

        # "Private variable" via automatic renaming (name-mangling): Double underscore variables (__age) are automatically renamed to hide  , stored internally as _Person__age
        self.__age = age

    def greet(self):
        # Public method, anyone can call this
        print(f"Hello, my name is {self.name}")

    def get_age(self):
        # Getter function to read private age safely
        return self.__age


class Student(Person):
    def __init__(self, name, address, age, student_id):
        # Call parent class constructor to setup name, address and age
        super().__init__(name, address, age)

        # Private variable only for Student, Python also rename it
        self.__student_id = student_id

    def show_address(self):
        # Child class allowed to access _address
        print(f"Address: {self._address}")

    def get_student_id(self):
        # Getter to access private student id
        return self.__student_id

    def greet(self):
        # Override greet from Person class
        print(f"Hi, I'm {self.name} and I'm a student!")


if __name__ == "__main__":
    s1 = Student("Alice", "123 Main St", 20, "S12345")

    # Public access, this one always ok
    print(s1.name)

    # Protected access, work but not good practice
    print(s1._address)

    # Wrong way, this will error because private variable hidden
    # print(s1.__age)

    # Correct way, use getter method
    print("Age:", s1.get_age())

    # Correct way also, use getter for student id
    print("Student ID:", s1.get_student_id())

    # Call overridden greet method
    s1.greet()
