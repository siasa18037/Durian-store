
# Account

class Account:
    def __init__(self, email, password, name, birthday ):
        self.__name = name
        self.__address_list = []
        self.__email = email
        self.__password = password
        self.__birthday = birthday
        
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_birthday(self):
        return self.__birthday
    
    # address
    def get_address_list(self):
        return self.__address_list
    
    def add_address(self, address):
        self.__address_list.append(address)
        
    def search_address_from_id(self, address_id):
        for address in self.__address_list:
            if address.get_address_id() == address_id:
                return address
        return None
    
    def delete_address_from_id(self, address_id):
        for address in self.__address_list:
            if address.get_address_id() == address_id:
                self.__address_list.remove(address)
                return True
        return False
