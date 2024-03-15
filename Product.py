class Product:
    def __init__(self, product_id, product_category , product_name , product_detail, product_amount, product_date_opening, product_quantity , product_img ):
        self.__product_name = product_name
        self.__product_id = product_id
        self.__product_category = product_category
        self.__product_detail = product_detail
        self.__product_amount = product_amount
        self.__product_date_opening = product_date_opening
        self.__product_quantity = product_quantity
        self.__product_img = product_img        
    def get_product_id(self):
        return self.__product_id
    
    def get_product_category(self):
        return self.__product_category
        
    def get_product_name(self):
        return self.__product_name
    
    def get_product_detail(self):
        return self.__product_detail
    
    def get_product_amount(self):
        return self.__product_amount
        
    def get_product_date_opening(self):
        return self.__product_date_opening
    
    def get_product_quantity(self):
        return self.__product_quantity
    
    def get_product_img(self):
        return self.__product_img
        
    def set_product_quantity(self, quantity):
        self.__product_quantity = quantity
        
    def checkout_product(self):
        self.__product_quantity = self.__product_quantity - 1
        
    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_category(self, product_category):
        self.__product_category = product_category

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_product_detail(self, product_detail):
        self.__product_detail = product_detail

    def set_product_amount(self, product_amount):
        self.__product_amount = product_amount

    def set_product_date_opening(self, product_date_opening):
        self.__product_date_opening = product_date_opening

    def set_product_img(self, product_img):
        self.__product_img = product_img