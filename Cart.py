class Cart:
    def __init__(self, cart_id):
        self.__cart_id = cart_id
        self.__product_list = []
        self.__promotion_list = []
        self.__amount = 0
        self.__status = 0
        # 0ยังไม่อยู่ในorder , 1เป็นorder
    
    def get_cart_status(self):
        return self.__status
        
    def set_cart_status(self, status):
        self.__status = status
    
    def get_cart_id(self):
        return self.__cart_id

    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount
    
    #calculates the amount
    def calculates_amount(self):
        self.__amount = 0
        for product in self.__product_list:
            self.__amount += product.get_product_amount()
        if self.__promotion_list is not None:
            promotion_totel = 0
            for promotion in self.__promotion_list:
                promotion_totel += self.__amount * promotion.get_calculate_rate()
            self.__amount = self.__amount - promotion_totel
        return self.__amount
        
    
    # product
    def get_product_list(self):
        return self.__product_list
    
    def add_product(self ,product):
        self.__product_list.append(product)
        return True
        
    def search_product_from_id(self, product_id):
        for product in self.__product_list:
            if product.get_product_id() == product_id:
                return product
        return None
    
    # promotion
    def get_promotion_list(self):
        return self.__promotion_list
    
    def add_promotion(self ,promotion):
        self.__promotion_list.append(promotion)
        return True
        
    def search_promotion_from_id(self, promotion_id):
        for promotion in self.__promotion_list:
            if promotion.get_promotion_id() == promotion_id:
                return promotion
        return None
    