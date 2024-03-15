import uvicorn
import random
import uuid

from datetime import datetime

from fastapi.responses import FileResponse , JSONResponse ,HTMLResponse 
from fastapi import FastAPI , HTTPException , Request , Form , Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile, File, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

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

# generate number
def generate_number():
    order_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return order_number



class Apple:
    def __init__(self):
        self.__product_list = []
        self.__promotion_list = []
        self.__customer_list = []
        self.__admin_list = []
        self.__help_list = []
        self.__category_list = []
        self.__payment_list = []

    #customer
    def add_customer(self, customer):
        self.__customer_list.append(customer)
        
    def get_customer_list(self):
        return self.__customer_list
        
    def search_customer_from_id(self, customer_id):
        for customer in self.__customer_list:
            if customer.get_customer_id() == customer_id:
                return customer
        return None
    
    def search_customer_from_email(self, customer_email):
        for customer in self.__customer_list:
            if customer.get_email() == customer_email:
                return customer
        return None
    
    
    # admin
    def add_admin(self, admin):
        self.__admin_list.append(admin)
    
    def search_admin_from_id(self, admin_id):
        for admin in self.__admin_list:
            if admin.get_admin_id() == admin_id:
                return admin
        return None

    def search_admin_from_email(self, admin_email):
        for admin in self.__admin_list:
            if admin.get_email() == admin_email:
                return admin
        return None
    
    #Category
    def add_category(self, category):
        self.__category_list.append(category)
        
    def search_category_from_id(self, category_id):
        for category in self.__category_list:
            if category.get_category_id() == category_id:
                return category
        return None
    
    def get_category_list(self):
        return self.__category_list
    
    def delete_category_from_id(self, category_id):
        for category in self.__category_list :
            if category.get_category_id() == category_id:
                self.__category_list.remove(category)
    
    def search_category_from_name(self, category_name):
        for category in self.__category_list:
            if category.get_category_name() == category_name:
                return category
        return None
    
  
    #products
    def add_product(self, product):
        self.__product_list.append(product)
        
    def search_product_from_id(self, product_id):
        for product in self.__product_list:
            if product.get_product_id() == product_id:
                return product
        return None
    
    def search_product_from_name(self, product_name):
        for product in self.__product_list:
            if product.get_product_name() == product_name:
                return product
        return None
    
    def get_product_list_from_category(self, product_category):
        product_list = []
        for product in self.__product_list:
            if product.get_product_category() == product_category:
                product_list.append(product)
        return product_list
    
    def get_all_product_info(self):
        product_all = []
        
        for product in self.__product_list:
            product_name = product.get_product_name()
            product_img = product.get_product_img()
            product_amount = product.get_product_amount()
            product_info = {
                "name" : product_name,
                "image" : product_img ,
                "amount" : product_amount
            }
            product_all.append(product_info)
        return product_all
    
    def get_product_list(self):
        return self.__product_list
    
    def get_product_list_by_category_name(self, category_name):
        product_list = []
        for product in self.__product_list:
            if product.get_product_category().get_category_name() == category_name :
                product_list.append(product.get_product_name())
        return product_list
    # update product quantity
    def update_product_quantity_from_cart(self, cart):
        product_list = cart.get_product_list()
        print(product_list)
        for product in product_list :
            product_name = product.get_product_name()
            product_quantity_old = product.get_product_quantity()
            product.checkout_product()
            product_quantity_new = product.get_product_quantity()
            text = product_name + " : " + str(product_quantity_old) + "->" + str(product_quantity_new)
            print(text)

    def edit_product_from_id(self, product_id , product_category , product_name , product_detail , product_amount , product_date_opening , product_quantity ,product_img):
        product = self.search_product_from_id(product_id)
        product.set_product_category(product_category)
        product.set_product_name(product_name)
        product.set_product_detail(product_detail)
        product.set_product_amount(product_amount)
        product.set_product_date_opening(product_date_opening)
        product.set_product_quantity(product_quantity)
        product.set_product_img(product_img)
    
    def delete_product_from_id(self, product_id):
        for product in self.__product_list :
            if product.get_product_id() == product_id:
                self.__product_list.remove(product)
                
        
    # payment
    def add_payment(self, payment):
            self.__payment_list.append(payment)
        
    def search_payment_from_id(self, payment_id):
        for payment in self.__payment_list:
            if payment.get_payment_id() == payment_id:
                return payment
        return None

    def get_payment_list(self):
        return self.__payment_list
    
    
    #promotion
    def add_promotion(self, promotion):
            self.__promotion_list.append(promotion)
        
    def search_promotion_from_id(self, promotion_id):
        for promotion in self.__promotion_list:
            if promotion.get_product_id() == promotion_id:
                return promotion
        return None
    
    def get_promotion_list(self):
        return self.__promotion_list

    def delete_promotion_from_id(self, promotion_id):
        for promotion in self.__promotion_list :
            if promotion.get_promotion_id() == promotion_id:
                self.__promotion_list.remove(promotion)
                

    # help
    def add_help(self, help):
            self.__help_list.append(help)
        
    def search_help_from_id(self, help_id):
        for help in self.__help_list:
            if help.get_help_id() == help_id:
                return help
        return None
    
    def get_help_list(self):
        return self.__help_list

    def delete_help_from_id(self, help_id):
        for help in self.__help_list :
            if help.get_help_id() == help_id:
                self.__help_list.remove(help)
        
        
    # order
    def get_all_order_list(self):
        all_order_list = []
        for customer in self.__customer_list :
            for order in customer.get_order_list() :
                all_order_list.append(order)
        return all_order_list
    
    def search_order_from_id(self, order_id):
        for customer in self.__customer_list :
            for order in customer.get_order_list() :
                if order.get_order_id() == order_id :
                    return order
        return None
    
    def delete_order_from_id(self, order_id):
        for customer in self.__customer_list :
            for order in customer.get_order_list() :
                if order.get_order_id() == order_id :
                    customer.delete_order_from_id(order_id)
        return None
    
    # seesion 
    # email check session
    def check_session(self,request: Request):
        if 'user_email' in request.session:
            return request.session['user_email']
        else:
            return None
    # type check session
    def check_session_type(self,request: Request):
        if 'user_type' in request.session:
            return request.session['user_type']
        else:
            return None
    
    
    # wook method
    # Add product to Cart
    def add_product_to_cart(self, product_id, customer_id):
        customer = self.search_customer_from_id(customer_id)
        product = self.search_product_from_id(product_id)
        if customer is None or product is None :
            return False
        else:
            cart = customer.search_cart_from_status()
            if cart.add_product(product) is not None:
                print("เพิ่มใส่ตากร้างเเล้ว")
                return True
            else:
                cart_id_new = generate_uuid_int_8_digits()
                customer.add_cart(Cart(int(cart_id_new)))
                if cart.add_product(product)is not None:
                    print("เพิ่มใส่ตากร้างเเล้ว")
                    return True
                else :
                    return False
        
    #login 
    def login(self , email ,password):
        if email is None or password is None:
            print("Error")
        else:
            for customer in self.__customer_list:
                if (email == customer.get_email()) and (password == customer.get_password()):
                    print("Login succesfull customer")
                    return "customer"
            for admin in self.__admin_list:
                if (email == admin.get_email()) and (password == admin.get_password()):
                    print("Login succesfull admin")
                    return "admin"
            print("login unsuccesfull")
            return None

    #Use promotion code
    def use_promotion_code(self, customer_id , promotion_code):
        customer = self.search_customer_from_id(customer_id)
        if customer is None :
            return False
        else:
            cart = customer.search_cart_from_status()
            for promotion in self.__promotion_list:
                if promotion.get_promotion_code() == promotion_code :
                    cart.add_promotion(promotion)
                    print("add code succesfull")
                    cart.calculates_amount()
                    return True
            print("dont have code")
            return False
                
    # submit to make Order
    def submit_to_make_order(self , customer_id , name , phone , address):
        customer = self.search_customer_from_id(customer_id)
        cart = customer.search_cart_from_status()
        cart.calculates_amount()
        
        cart.set_cart_status(1)
        
        # สร้างวันที่ปัจจุบัน
        current_date = datetime.now().strftime("%B %d, %Y")
        
        order_id = generate_number()
        if customer.add_order(Order(order_id, current_date, cart , name , phone ,address)) :
            cart_id_new = generate_uuid_int_8_digits()
            customer.add_cart(Cart(int(cart_id_new)))
            
            print(f"เลขคำสั่งซื้อ : {order_id} , cart_id_new : {cart_id_new}")
            return order_id
        else :
            print("Make Order Error")
            cart_id_new = generate_uuid_int_8_digits()
            customer.add_cart(Cart(int(cart_id_new)))
            return None
        
    # payment
    def payment(self , customer_id , order_id , payment_id):
        customer = self.search_customer_from_id(customer_id)
        order = customer.search_order_from_id(str(order_id))
        payment =  self.search_payment_from_id(payment_id)
        
        # print(customer)
        # print(order.get_status())
        if customer is None or order is None :
            return False
        else :
            cart = order.get_cart()
            amount = cart.get_amount()
      
            if payment.get_payment_type() == "Card" :
                payment.payment_card(amount)
                # จ่าตั้งเเล้ว
                order.set_status(1)
                # print(order.get_status())
            elif payment.get_payment_type() == "QR" :
                payment.payment_qr(amount)
                # จ่าตั้งเเล้ว
                order.set_status(1)
                # print(order.get_status())
            elif payment.get_payment_type() == "Bank" :
                payment.payment_bank(amount)
                # จ่าตั้งเเล้ว
                order.set_status(1)
                # print(order.get_status())
                
            if order.get_status() == 1 :
                self.update_product_quantity_from_cart(cart)
                print("payment successful")
                return True
            else:
                print("payment Unsuccessful")
                return False
            
            # ระบบคราวๆๆ
            # # ตามหลักต้องมีระบบของธนาคารมายืนยันด้วย เเต่จะให้ pass
            # if order.payment() :
            #     print("payment successful")
            #     return True
            # else :
            #     print("payment Unsuccessful")
            #     return False
    
         
         


