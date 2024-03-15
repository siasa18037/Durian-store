
class Payment:
    def __init__(self,payment_id , payment_type , name , payment_id_bank , bank , payment_detail , status , img):
        self.__payment_type = payment_type
        self.__payment_id = payment_id
        self.__payment_id_bank = payment_id_bank
        self.__bank = bank
        self.__name = name
        self.__payment_detail = payment_detail
        self.__status = status
        self.__img = img

    def get_payment_type(self):
        return self.__payment_type
    
    def get_payment_id(self):
        return self.__payment_id
    
    def get_payment_id_bank(self):
        return self.__payment_id_bank
    
    def get_payment_detail(self):
        return self.__payment_detail
    
    def get_bank(self):
        return self.__bank
    
    def get_name(self):
        return self.__name
    
    def get_img(self):
        return self.__img
    
    def get_status(self):
        return self.__status
    
    def set_status(self ,status_new):
        self.__status = status_new
        
        
    def payment_qr(self , amount):
        return True
    
    def payment_card(self , amount):
        return True
    
    def payment_bank(self , amount):
        return True