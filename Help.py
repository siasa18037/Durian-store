class Help:
    def __init__(self, help_id, help_title, help_detail):
        self.__help_id = help_id
        self.__help_title = help_title
        self.__help_detail = help_detail

    def get_help_id(self):
        return self.__help_id

    def get_help_title(self):
        return self.__help_title

    def get_help_detail(self):
        return self.__help_detail
