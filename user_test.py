import unittest # importing the unittest module
from user import User #importing the user class

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each test case
        '''
        self.new_user = User("Juliet","Mwiti","jules@gmail.com")
     
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name,"Juliet")
        self.assertEqual(self.new_user.password,"Mwiti")
        self.assertEqual(self.new_user.email,"jules@gmail.com")
      
    def test_save_user(self):
        '''
        test_save_user test case to test if the user is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
      
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple users
        object to our user-list
        '''
        self.new_user.save_user()
        test_user = User("mike","password","mike@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
       
    def tearDown(self):
        '''
        tearDown method that does clean up after test case has run
        '''
        User.user_list =  []
        
    def test_display_user(self):
        '''
        test_display_user returns list of password users
        '''
        self.assertEqual(User.display_users(),User.user_list)
        
    def test_login_user(self):
        '''
        test_login_user to login a user
        '''
           
        self.new_user.save_user()
        test_user=User("Emma","james","james@gmail.com")
        test_user.save_user()
        logged_in=User.user_verified("Emma","james","james@gmail.com")
          
        self.assertTrue (logged_in)
    
          

         
      
        
        
if __name__ == '__main__':
    unittest.main()