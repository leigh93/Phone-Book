import unittest  #import unittest module from python
from contact import Contact #import contact class from contact.py
import pyperclip
class TestContact(unittest.TestCase): #create test class subclass that inherits from unittest.Testcase its parent class which we pass in as parameters defines testcases for the Contact class behaviours
 
#  #test one ensure objects are being instantiated correctly
#     1. create instance 
    def setUp(self):
        self.new_contact = Contact("Sherlock", "Holmes", "0712345678", "detective@mail.com")  #create contact object
#   2. create test
    def test_init(self):       #test to check if class is being initialized properly
        self.assertEqual(self.new_contact.first_name,"Sherlock")
        self.assertEqual(self.new_contact.last_name,"Holmes")
        self.assertEqual(self.new_contact.number,"0712345678")
        self.assertEqual(self.new_contact.email,"detective@mail.com")

    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1) 
    
    # create tear down method to clear instances after you run the code 
    def tearDown(self):
        Contact.contact_list = []

    
    def test_save_multiple(self):
        self.new_contact.save_contact()
        test_contact=Contact("test", "user", "978899877766", "testuser@gmail.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        test_contact = Contact("test", "user","700000000", "user@mail.com")
        test_contact.save_contact()
        test_contact2=Contact("test", "user", "978899877766", "testuser@gmail.com")
        test_contact2.save_contact()
        test_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_by_number(self):
        test_contact = Contact("test", "user","700000000", "user@mail.com")
        test_contact.save_contact()
        found_contact = Contact.find_by_number("700000000")
        self.assertEqual(found_contact.email,test_contact.email)

    def test_contact_exists(self):
        test_contact = Contact("test", "user","700000000", "user@mail.com")
        test_contact.save_contact()
        contact_exists = Contact.contact_exist("700000000")
        self.assertTrue(contact_exists)
    
    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(),Contact.contact_list) 
    
    #create method to copy and paste an email
    def test_copy_email(self):
        self.new_contact.save_contact()
        Contact.copy_email("0712345678")
        self.assertEqual(self.new_contact.email,pyperclip.paste())


if __name__=='__main__':
    unittest.main()
        


