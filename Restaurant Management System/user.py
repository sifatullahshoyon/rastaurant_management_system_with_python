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

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.cart = None
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name):
        item = restaurent.menu.find_item(item_name)
        if item:
            pass
        else:
            print('Item Not Found!')
    
    def view_cart(self):
        print('\n**** View Cart ****\n')
        print('Name\tPrice\tQuantity')

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee("rahim", "rahim@gmail.com", 12456, "Dhaka", 23, "Chef", 12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        
    
    # def add_employee(self, name, email, phone, address, age, designation, salary):
    #     employee = Employee(name, email, phone, address, age, designation, salary) # Employee class ar ekta object toiri hoye jabe.
    #     self.employees.append(employee)
    #     # print(f"{employee.name} is added!!")
    #     print(f"{name} is added!!")

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
    
    def view_employee(self, restaurent):
        restaurent.view_employee()
    
    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)
    
    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta hocche amader database
        self.menu = FoodItem()  
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def view_employee(self):
        print("\n------ Employee List ------\n")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

class Menu:
    def __init__(self):
        self.items = [] # items er database
    
    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted.")
        else:
            print("Item Not Found.")
    
    def show_menu(self):
        print('\n****** Menu ******\n')
        print('Name\tPrice\tQuantity\n')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

ad = Admin("Karim", "karim@gmail.com", "123456", "Dhaka")
mn = Menu()
item = FoodItem('Pizza', 12.54, 10)
mn.add_menu_item(item)
mn.show_menu()