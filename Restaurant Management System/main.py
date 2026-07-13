from food_item import FoodItem
from user import Customer, Admin, Employee
from orders import Order
from restaurent import Restaurent

mamar_restaurent = Restaurent('Mamar Restaurent')

def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'Welcome {customer.name}')
        print(f'1. View Menu')
        print(f'2. Add item to cart')
        print(f'3. View Cart')
        print(f'4. PayBill')
        print('5. Exit')

        choice = int(input('Enter Your Choice : '))

        if choice == 1:
            customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input('Enter item name : ')
            item_quantity = int(input('Enter Item Quantity : '))
            customer.add_to_cart(mamar_restaurent, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print('Invalid Input')


#! Admin
def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'Welcome {admin.name}')
        print(f'1. Add New Item')
        print(f'2. Add New Employee')
        print(f'3. View Employee')
        print(f'4. View Items')
        print(f'5. Delete Item')
        print(f'6. Exit')

        choice = int(input('Enter Your Choice : '))

        if choice == 1:
            item_name = input('Enter Item Name : ')
            item_price = int(input('Enter Item Price : '))
            item_quantity = int(input('Enter Item Quantity : '))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)
        elif choice == 2:
            name = input('Enter Employee Name : ')
            phone = input('Enter Employee Phone Number : ')
            email = input('Enter Employee Email Address : ')
            designation = input('Enter Employee designation : ')
            salary = input('Enter Employee Salary : ')
            address = input('Enter Employee Address : ')
            admin.add_employee(name, email, phone, address, designation, salary)
        elif choice == 3:
            admin.view_employee(mamar_restaurent)
        elif choice == 4:
            admin.view_menu(mamar_restaurent)
        elif choice == 5:
            item_name = input('Enter Item Name : ')
            admin.remove_item(mamar_restaurent, item_name)
        elif choice == 6:
            break
        else:
            print('Invalid Input')