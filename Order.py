
class Order:
    def __init__(self, order_id, order_date, cart , name, phone ,address):
        self.__order_id = order_id
        self.__order_date = order_date
        # 0 สร้างoderยังไม่จ่ายตัง , 1 จ่ายตังเเล้ว , 2 ส่งของเเล้ว ,9 ยกเลิกเเล้ว
        self.__status = 0 
        self.__cart = cart
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__tracking_number = None
        self.__logistic = None

    def get_order_id(self):
        return self.__order_id
    
    def get_order_date(self):
        return self.__order_date
    
    def get_status(self):
        return self.__status
    
    def set_status(self,status):
        self.__status = status
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_status_text(self):
        if self.__status == 0:
            return "ยังไม่ชำระเงิน"
        elif self.__status == 1:
            return "ชำระเรียบร้อยเเล้ว"
        elif self.__status == 2:
            return "ส่งพัสดุแล้ว"
        elif self.__status == 9:
            return "ยกเลิกเเล้ว"
        
    def get_address(self):
        return self.__address
    
    def get_tracking_number(self):
        return self.__tracking_number
    
    def set_tracking_number(self, tracking_number):
        self.__tracking_number = tracking_number
    
    def get_logistic(self):
        return self.__logistic
    
    def set_logistic(self, logistic):
        self.__logistic = logistic
        
    # cart
    def get_cart(self):
        return self.__cart
    
   
   