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
        self.cart = Order()
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item Quantity Exceeded!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('Item Added.')
        else:
            print('Item Not Found!')
    
    def view_cart(self):
        print('\n**** View Cart ****\n')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price : {self.cart.total_price}')
    
    def pay_bill(self):
        print(f'Total {self.cart.total_price} Paid Successfully.')
        self.cart.clear()
        
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







ad = Admin("Karim", "karim@gmail.com", "123456", "Dhaka")
mama_res = Restaurent('Mama Restaurent')
mn = Menu()
item = FoodItem('Pizza', 12.54, 10)
item2 = FoodItem('Burger', 10, 30)
admin = Admin('Rahim', 'rahim@gmail.com', 975236, 'Dhaka')
admin.add_new_item(mama_res, item)
admin.add_new_item(mama_res, item2)
mn.add_menu_item(item2)
mn.show_menu()

customer1 = Customer('Rahim', 'rahim@gmail.com', 975236, 'Dhaka')
customer1.view_menu(mama_res)

item_name = input("Enter item Name : ")
item_quantity = int(input("Enter Item Quantity : "))

customer1.add_to_cart(mama_res, item_name, item_quantity)
customer1.view_cart()