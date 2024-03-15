class Address:
    def __init__(self, address_id, address_name, address_phone, address_homeid_detail, address_sub_area, address_district, address_province, address_postcode):
        self.__address_id = address_id
        self.__address_name = address_name
        self.__address_phone = address_phone
        self.__address_homeid_detail = address_homeid_detail
        self.__address_sub_area = address_sub_area
        self.__address_district = address_district
        self.__address_province = address_province
        self.__address_postcode = address_postcode

    def get_address_id(self):
        return self.__address_id

    def get_address_name(self):
        return self.__address_name

    def get_address_phone(self):
        return self.__address_phone

    def get_address_homeid_detail(self):
        return self.__address_homeid_detail
    
    def get_address_sub_area(self):
        return self.__address_sub_area

    def get_address_district(self):
        return self.__address_district

    def get_address_province(self):
        return self.__address_province

    def get_address_postcode(self):
        return self.__address_postcode
    
    
        
