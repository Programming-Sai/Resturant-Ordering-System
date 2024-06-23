import random 
import os 
from tabulate import tabulate
import time 
import string 




'''
First class:
  Order Class. For making and adjusting orders 
'''


class Order: 
    def __init__(self):
        self.item = ''  
        self.quantity = 0
        
   
        
    def add_order(self, menu, selection):        
        """  
            Adds an Order.
    
            Parameters:
            menu(list): holds a collection of food items and their prices
            selection(int): tells which items to add to order 
            
            Returns:
            tuple: this holds separately, a list of the food items and their quantities 
        """ 
        self.item = (menu[selection])
        quantity = ''
        while quantity not in [str(a) for a in range(10)]:
            quantity = input('And How Many? ')           
        self.quantity = (int(quantity)) 
        return (self.item, self.quantity)
        
        
            
    def remove_order(self, items, s):  
        """  
            Removes an Order.
    
            Parameters:
            items(list): holds a collection of food items
            s(int): tells which items to remove from the order 
            
            Returns:
            list:  this holds the food items 
        """   
        items.pop(s) 
        check = ''
        while check not in ['Y', 'N']:
            check = input('\nWould that be all? (Y/N)  ').upper()        
        if check == 'Y':
            pass                      
        elif check == 'N':               
            for i in range(len(items)):
                print(i+1, items[i])
            s = ''
            while s not in [str(a) for a in range( len(items) + 1)]:
                s = input('\nAnything Else? ')
            s = int(s)     
            self.remove_order(items, (s-1))                
        return (items)
      
                    
    def view_order(self, customer, item, quantity):
          """  
            Displays an Order.
    
            Parameters:
            customer(class instance of Customer Class):  Provides the name of the customer who makes the order
            items(list): holds a collection of food items
            quantity(list): holds a collection of food item quantities 
            
            Returns: None 
          """ 
          print(f"\nOrder Summary for {customer}")
          print('================================\n')
          header = ['Food Item', 'Quantity']         
          data = [((str(i + 1) + ". " + item[i] ), quantity[i]) for i in range(len(item))]        
          print(tabulate(data, header, tablefmt = 'csv'))








'''
Seacond class:
  Menu Class. For Decomposing and showing Menus 
'''




class Menu:
   def  __init__(self, menu): 
       self.menu = menu
       self.name = []
       self.price = []
       self.menu_items_list = [] 
       with open(menu, 'r') as m:
           menu_items = m.readlines()  
           
           for item in menu_items:
               self.menu_items_list.append(item.rstrip('\n'))

       
   def menu_items(self):
       """  
            Obtains the Food Item part of a menu.
    
            Parameters: None

            Returns: 
            str: food item name 
       """ 
       for item in self.menu_items_list:
         self.name.append(item[:item.find(',')])
       return self.name


   def menu_item_prices(self):
       """  
            Obtains the Food Item Price art of a menu.
    
            Parameters: None

            Returns: 
            str: food item price 
       """ 
       for item in self.menu_items_list:
         self.price.append(float(item[item.find(',') + 1:]))
       return self.price
     
     
       
     
     
   def view_menu(self):
       """  
            Displays entire Menu.
    
            Parameters: None

            Returns: 
            dictionary:holds the food item name  and prices
       """ 
       print(( "\033[1m" + "Menu" + "\033[0m").center(35))
       print('=============================\n')
       header = ["", 'Food Item', 'Price']         
       data = [(str(i+1) , self.name[i] , "$" + str(self.price[i])) for i in range(len(self.name))]        
       print(tabulate(data, header, tablefmt = 'csv'))
       print('\n')
       return {self.name: self.price for self.name, self.price in zip(self.name, self.price)}

     
     



'''
Third class:
   Payment Class. For Making payments 
'''



class Payment:
   def __init__(self):
       self.ordered = False
       self.transaction_status = 'pending'
       self.payment_method = ''
       self.total_amt = round(0, 2)
       
    
   def payment_status(self, expense):
       """  
            Updates the payment status .
    
            Parameters:  
            expense (dictionary):Holds food item name that is linked to a list holding the quantity and price

            Returns: 
            string: Transaction status 
       """ 
       self.transaction_status = 'successful'if self.total_amt == expense and self.ordered else 'failed'
       return self.transaction_status
           
           
           
           
           
   def total_expense(self, expenses): 
       """  
            Calculates the total expenses of an order.
    
            Parameters:  
            expense (dictionary):Holds food item name that is linked to a list holding the quantity and price

            Returns: 
            int: Total expense 
       """ 
       for expense in expenses:
           self.total_amt += (expenses[expense][0] * expenses[expense][1])         
       return self.total_amt 
   
   
   def get_payment_method(self):
       """  
            Obtains the method of payment from the customer .
    
            Parameters: None

            Returns: 
            string: Total expense 
       """ 
       payment_method = ''
       payment_methods = ["Cash", "Credit Card"]
       print('\n\n')
       for l, x in enumerate(payment_methods, start = 1):
           print(f'{l}. {x}')
       while payment_method not in [str(a) for a in range(1, 3)]:
           payment_method = input("\n\nHow Would you Like To Pay; ")
       self.payment_method = payment_methods[int(payment_method)-1]
       return self.payment_method
   
   
   
   
   
   def tax_inclusion(self, tax_rate):
       """  
            Includes Taxes, if any

            ParameteNone
            tax_rate(float): self explanatory 

            Returns: 
            int: Total expense plus taxes
       """ 
       self.total_amt *= (1+tax_rate)
       return self.total_amt
       
       
       
       
       
   def show_receipt(self, expenses, balance, method):
       """  
            Displays the Receipt After Payment .
    
            Parameters:
            expenses(dictionary): Holds food item name that is linked to a list holding the quantity and price
            balance(float): the change, after a cash payment is made
            method(string): the method of payment (Cash / Credit Card)

            Returns: None 
       """ 
       header = ['Food Item', 'Quantity', 'Price', 'Total']
       data = [(expense, expenses[expense][1], ("$" + str(expenses[expense][0])), ("$" + str(round((expenses[expense][1] * expenses[expense][0]), 2)))) for expense in expenses]
       table = tabulate(data, header, tablefmt = 'grid')
       print('\n\n')
       print(f"Receipt for Purchases Made by {customer.name}\n*************************************".center(35))
       print(table)
       print (f'Total Bill: ${self.total_amt}')
       print('' if balance == None else f'Balance: ${balance}')
       print('Payment Method: ', method)








'''
Last class:
   Customer Class. For Simulating customers
'''

class Customer:
    def __init__(self, name):
        self.name = name
        self.table_number = random.randint(1, 20)
        self.order = []
        self.haveOrdered = False




    def view_menu(self):
        """  
            Displays the Menu to the Customer .
    
            Parameters: None
            
            Returns: 
            tuple: food item names, food item prices and a dictionary that holds the food item name  and prices
        """ 
        menu = Menu('Menu.txt')
        items = menu.menu_items()
        prices = menu.menu_item_prices()
        food = menu.view_menu()
        return items, prices, food
        
        
        
    @staticmethod
    def yes_no_input(text):
        """  
            Static Method, that allows for the selection of Yes/ No answers.
    
            Parameters:
            text(string): Prompts the user in what to enter

            Returns: 
            tuple: tuple holding 'Y', 'N' and the user's choice
        """ 
        check = ''
        while check not in ['Y', 'N']:
           check = input(text + '(Y/N)  ').upper()
        if check == None:
            return (('Y', 'N'), '')
        else:
            return (('Y', 'N'), check)
       
        
        
    def place_order(self):   
        """  
            Allows the user the make orders
    
            Parameters: None
            
            Returns: 
            tuple: Food item prices and a dictionary that holds the food item quantities ordered and prices 
        """ 
        items, prices, food = self.view_menu()        
        def make_order(items):    
                order = Order()                            
                selection = ''
                while selection not in [str(a) for a in range( len(items) + 1)]:
                    selection = input('What would you be ordering? ')
                selection = int(selection)               
                order.add_order(items, (selection-1))
                self.order.append(order)
                options, check = self.yes_no_input('\nWould that be all?')                  
                if check == options[0]:
                    choices, answer = self.yes_no_input('\nWould You Like To Cancel An Order?')
                    if answer == choices[0]:
                       for i in range(len(self.order)):
                           print(i+1, self.order[i].item)
                       items = [self.order[a].item for a in range(len(self.order))]
                       s = ''
                       while s not in [str(a) for a in range( len(self.order) + 1)]:
                          s = input('\nWhich order would you be cancelling? ')
                       s = int(s)                  
                       next = order.remove_order(items, (s-1))
                       self.order = [self.order[x] for x in range(len(self.order)) if self.order[x].item in next]                 
                    else:                  
                       print('order conpleted')
                       return (order, self.order)
                elif check == options[1]:
                    make_order(items)
                    return (order, self.order)
                    
        order, self.order = make_order(items)
        self.haveOrdered = True 
        os.system('cls' if os.name == 'nt' else 'clear')
        order.view_order(self.name, [a.item for a in self.order], [b.quantity for b in self.order])                  
        return prices, food                
                





    def make_payment(self, all):
        """  
            Allows the user the make payments
    
            Parameters:
            all(tuple):Food item prices and a dictionary that holds the food item quantities ordered and prices 
            
            Returns: None
        """ 
        print(''*9000)
        prices, food = all
        payment = Payment()         
        items = [a.item for a in self.order]        
        quantity = [b.quantity for b in self.order] 
        prices =  [food[c] for c in items]
        expense = {items :(prices, quantity) for items , (prices, quantity) in zip(items, zip(prices, quantity))}
        if  self.haveOrdered:
             print(f'\nBill: ${payment.total_expense(expense)}')             
             method = payment.get_payment_method()
             if method == 'Cash':                               
                 while True:
                     try:
                         cash = float(input('\nPlease Enter Your Fee: $'))
                         if cash < payment.total_amt:
                             print('\nTotal Bill Exceeds Current Input.\nPlease Try Again')
                         else:
                             balance = round((cash - payment.total_amt), 2)
                             break 
                     except ValueError:
                         continue 
             else:
                 print('\nTransaction successful')
                 balance = None
             payment.show_receipt(expense, balance, method)
        else:
            print('Please Make Your Order.')
            



                   
def get_name(text):   
    """  
            Allows the user to enter their name in the Customer class
    
            Parameters: 
            text(string): Prompts the user on what information to give
            
            Returns: 
            string: name of the user
    """ 
    name = '' 
    while name in [str(a) for a in range(10)] or name in string.punctuation:
        name = input(text)
    if ' ' in name:
       names = name.split(' ') 
       names = [name.capitalize() for name in names]
       name = ' '.join(names)
    else:
       name = name.capitalize()
    return name
                                    
                                                                                               


if __name__ == '__main__':
    print('Welcome!!\n')
    customer = Customer(get_name("What's your name please? "))
    print("Please Have a Sit and \nLook Through The Menu.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    money = customer.place_order()
    customer.make_payment(money)