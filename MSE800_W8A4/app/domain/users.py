"""
DOMAIN: USERS
OOP:
- Abstraction: User is abstract
- Inheritance: Admin/Customer inherit User
- Polymorphism: is_admin(), can_manage_cars()
- Encapsulation: fields protected with properties
"""

from abc import ABC, abstractmethod


class User(ABC):  # User is a base class template (cannot be used directly)
    def __init__(self, user_id: int, name: str, email: str, role: str) -> None:
        # This function runs when a User/Admin/Customer object is created.
        # ENCAPSULATION: These values are kept private so they cannot be changed accidentally from outside the class.
    
        self._user_id = int(user_id)            # Keep user_id as integer so it is always a number
        self._name = name.strip()               # remove extra space
        self._email = email.strip().lower()     # clean email, no duplicate
        self._role = role                       # Save the role text (ADMIN or CUSTOMER)

    @property
    def user_id(self) -> int: # This makes user_id readable like: user.user_id (looks like a field but it is a method)
        # ENCAPSULATION: Other parts of the program can read the ID,  but cannot directly change it.
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def role(self) -> str:
        return self._role

    @abstractmethod
    # ABSTRACTION: This method defines what all users must support, but does not explain how it works.
    def is_admin(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def can_manage_cars(self) -> bool:
        raise NotImplementedError


class Admin(User): # admin is a user
    def __init__(self, user_id: int, name: str, email: str) -> None:
        super().__init__(user_id, name, email, role="ADMIN")

    def is_admin(self) -> bool:
        return True  # admin always true

    def can_manage_cars(self) -> bool:
        return True # admin can manage car


class Customer(User): # customer is also user
    def __init__(self, user_id: int, name: str, email: str, loyalty_points: int = 0) -> None:
        super().__init__(user_id, name, email, role="CUSTOMER") # set role customer
        self._loyalty_points = int(loyalty_points)  # keep points safe

    @property
    def loyalty_points(self) -> int:
        return self._loyalty_points # return customer points

    def is_admin(self) -> bool:
        return False # customer not admin

    def can_manage_cars(self) -> bool:
        return False # customer cannot manage car
