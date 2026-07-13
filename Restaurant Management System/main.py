from food_item import FoodItem
from menu import Menu
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