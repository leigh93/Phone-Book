import pyperclip

class Contact:    #class that generates new instances of contacts
   
    contact_list=[]
        
    def __init__(self,first_name, last_name, number, email):  #init method defines properties of the class

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
    
    # 1. create save method
    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    @classmethod   #tells the python interpreter that this method applies to the entire class
    def find_by_number(cls, number):    #(cls) refers to entire class
        for contact in cls.contact_list:
            if contact.number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        for contact in cls.contact_list:
            if contact.number == number:
                return True
            else:
                return False
    
    @classmethod
    def display_contacts(cls):
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)     