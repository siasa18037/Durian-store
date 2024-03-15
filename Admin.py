from Account import *

class Admin(Account):
    def __init__(self, admin_id, email, password, name, birthday ):
        super().__init__(email, password, name, birthday )
        self.__admin_id = admin_id

    def get_admin_id(self):
        return self.__admin_id
    
    