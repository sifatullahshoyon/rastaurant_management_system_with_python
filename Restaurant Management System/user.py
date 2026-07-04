# Customer
# Employee
# Admin

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        pass   