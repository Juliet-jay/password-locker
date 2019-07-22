import unittest
from user import User #importing the User class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args:
        unnitest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user=User("Juliet","_patrick21")

    def test_init(self):
        '''
        test init test case to test if the obj is initialized correctly
        '''
        self.assertEqual(self.new_user.name,"Juliet")
        self.assertEqual(self.new_user.password,"_patrick21")

    def test_save_user(self):
        '''
        test save user to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving a user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test save multiple to check if we can save multiple user obj to our user_list
        '''

        self.new_user.save_user()
        test_user=User("Tommy","linet_5")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
        '''
        tearDown method that cleans up after each test has run
        '''
        User.user_list=[]  

    def test_display_users(self):
        '''
        test_display_users returns list of password locker users
        ''' 

        self.assertEqual(User.display_users(),User.user_list)

    def test_login_user(self):
        '''
        test_login_ to login a user
        '''
        #confirms if as vallid credentials are entered
        self.new_user.save_user()
        test_user=User("Eric","Nate_3")
        test_user.save_user()
        logged_in=User.user_verified("Eric","Nate_3")

        self.assertTrue(logged_in)





        
if __name__=='__main__':
    unittest.main()
