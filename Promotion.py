class Promotion:
    def __init__(self, promotion_id , promotion_code , promotion_detail, promotion_name, calculate_rate):
        self.__promotion_id = promotion_id
        self.__promotion_detail = promotion_detail
        self.__promotion_name = promotion_name
        self.__calculate_rate = calculate_rate
        self.__promotion_code = promotion_code

    def get_promotion_id(self):
        return self.__promotion_id
    
    def get_promotion_detail(self):
        return self.__promotion_detail
    
    def get_promotion_name(self):
        return self.__promotion_name
    
    def get_promotion_code(self):
        return self.__promotion_code
    
    def get_calculate_rate(self):
        return self.__calculate_rate
    