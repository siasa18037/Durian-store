
class Category:
    def __init__(self, category_id, category_name, category_detail ,img):
        self.__category_id = category_id
        self.__category_name = category_name
        self.__category_detail = category_detail
        self.__category_img = img
        
    def get_category_id(self):
        return self.__category_id
    
    def get_category_name(self):
        return self.__category_name
    
    def get_category_detail(self):
        return self.__category_detail
    
    def get_category_img(self):
        return self.__category_img
