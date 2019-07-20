import unittest
from credential import Credential


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("user_name", "password", "email@ms.com")  # create credential object

