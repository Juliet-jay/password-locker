import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours
    Arg:
        unittest.TestCase:Test case class that helps in creating test cases
    '''

    def setUp(self):
        '''
        setUp method to run before each test case
        '''

        #create a credential obj
        self.new_credential=Credential("james","Nathan","Mike","Bonface")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list=[]


    def test_init(self):
        '''
        test init test case to test if the obj is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"James")
        self.assertEqual(self.new_credential.user_password,"Nathan") 
        self.assertEqual(self.new_credential.credential_name,"Mike")
        self.assertEqual(self.new_credential.credential_password,"Bonface")


    def test_save_credential(self):
        '''
        test_save_credential to test if the credential obj is saved into the credential list
        '''

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)


    def test_save_multiple_credential(self):
        '''
        tesr save multiple credential to test if we can save multiple credentials to the credential list
        '''

        self.new_credential.save_credential()
        test_credential=Credential("Picknpick","Jetplan","Finance","European")

        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2) 

    def test_delete_credential(self):
        '''
        delete credential to test if we can remove a credential from the credential list
        '''
        self.new_credential.save_credential()

        test_credential=Credential("Homeland","NYA","FBI","Csi")  
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_display_credential(self):
        '''
        display credential that returns a list of a users credentials
        '''

        self.new_credential.save_credential()

        test_credential=Credential("Fenamial","Henry","Jason","_Kenneth")
        test_credential.save_credential()

        test_credential=test_credential=Credential("Fenamial","Henry","Fatandol","Kenneth")
        test_credential.save_credential()

        self.assertEqual(len(Credential.display_credential("Fenamial","Kenneth")),2)

    def test_auto_generate_password(self):
        '''
        test auto generate to see if we can generate a password for a user credentials
        '''
        #password length
        pass_length=8

        #variable to hold the password
        generated_password=Credential.generate_password(pass_length)

        self.assertEqual(len(generated_password),pass_length)  

    def test_find_credential(self):
        '''
        test to see if we can search for and fetch a credential by its name
        '''

        self.new_credential.save_credential()
        test_credential=Credential("Kathure","Cia","Homeland","Collins")

        test_credential.save_credential()

        found_credential=Credential.find_by_name("Kathure","Homeland","Collins")
        self.assertEqual(found_credential.credential_password,test_credential.credential_password)

    def test_check_existing_credential(self):
        '''
        test to check if we can return a boolean if we can/cannot find a credential
        '''


        self.new_credential.save_credential()
        test_credential=Credential("Gelly","Mary","Marthor","Susan_may")

        test_credential.save_credential()

        credential_exists=Credential.credential_exists("Gelly","mary","Marthor")
        self.assertTrue(credential_exists)




if __name__=='__main__':
    unittest.main()        
