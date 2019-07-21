import unittest
from credential import Credential


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("user", "password", "email@gmail.com")  # create credential object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []
        
    def test_init(self):
        """
        test_init test case to test if the object is properly initialized
        """
        self.assertEqual(self.new_credential.user_name, "user")
        self.assertEqual(self.new_credential.password, "password")
        self.assertEqual(self.new_credential.email, "email@gmail.com")
        
    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saved into
         the credential list
        """
        self.new_credential.save_credential()  # save the new credential
        self.assertEqual(len(Credential.credential_list), 1)
        
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our user_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("user","password","email@gmail.com") # new account
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
            
    def test_find_credential_by_credential_name(self):
        '''
        test to check if we can find an user by user_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("user","password","email@gmail.com") # new account
        test_credential.save_credential()

        found_credential = Credential.find_by_name("user")

        self.assertEqual(found_credential.email,test_credential.email)  
        
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("user","password","email@gmail.com") # new account
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("email@gmail.com")
        self.assertTrue(credential_exists)    
           
    def test_display_credential(self):
        """
        method that returns a list of saved credential
        """
        self.assertEqual(Credential.display_credential(), Credential.credential_list)


if __name__ == '__main__':
     unittest.main()     
    