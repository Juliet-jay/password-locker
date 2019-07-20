import unittest
from credential import Credential


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("user_name", "password", "email@gmail.com")  # create credential object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []