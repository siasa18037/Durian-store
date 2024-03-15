import uvicorn
import random
import uuid

from main import *
from BaseModel import *
from Account import *
from Product import *
from Promotion import *
from Order import *
from Customer import *
from Payment import *
from Apple import *
from Apple import *
from Cart import *
from Category import *
from Help import *
from Address import *


def generate_uuid_int_8_digits():
    uuid_int = int(uuid.uuid4().hex, 16)
    uuid_int_8_digits = uuid_int % 10**8
    return uuid_int_8_digits

  
# Customer
class Customer(Account):
    def __init__(self, customer_id, email, password, name, birthday ):
        super().__init__(email, password, name, birthday )
        self.__customer_id = customer_id
        self.__order_list = []
        self.__cart_list = []
        
        # create cart_id for firsttime
        self.__cart_id = generate_uuid_int_8_digits()
        self.add_cart(Cart(self.__cart_id))
        

    # Account
    def get_customer_id(self):
        return self.__customer_id
    
    # cart
    def add_cart(self , cart):
        self.__cart_list.append(cart)
        
    def get_cart(self):
        return self.__cart
    
    def search_cart_from_id(self, cart_id):
        for cart in self.__cart_list:
            if cart.get_cart_id() == cart_id:
                return cart
        return None
    
    def search_cart_from_status(self):
        for carts in self.__cart_list:
            if carts.get_cart_status() == 0:
                return carts
        return None

    
    # order
    def get_order(self):
        return self.__order_list
    
    def add_order(self ,order):
        self.__order_list.append(order)
        return True
        
    def search_order_from_id(self, order_id):
        for order in self.__order_list:
            if order.get_order_id() == order_id:
                return order
        return None
    
    def get_order_list(self):
        return self.__order_list
    
    def get_order_id_list(self):
        return [ order.get_order_id() for order in self.__order_list]
            
    def delete_order_from_id(self, order_id):
        for order in self.__order_list:
            if order.get_order_id() == order_id:
                self.__order_list.remove(order)
                return True
        return False
