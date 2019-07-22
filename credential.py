'''
Import string module that contains various ASCII characters of all cases
Import random module to perform random generations
'''

import random
import string

class Credential:
    '''
    Class that generates instances of user credentials
    '''

    credential_list=[]

    def __init__(self,user_name,user_password,credential_name,credential_password):
        '''
        __init__ method to define the properties of a user credential
        Args:
            user_name:name of the user
            user_password:password locker of a user
            credential_name:name of an account
            credential_password:password for the account
        '''

        self.user_name=user_name
        self.user_password=user_password
        self.credential_name=credential_name
        
        
        self.credential_password=credential_password

    def save_credential(self):
        '''
        Method that saves a credential obj to the credential list
        '''

        Credential.credential_list.append(self) 

    def delete_credential(self):
        '''
        Method that deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self) 


    @classmethod
    def display_credential(cls,name,password):
        '''
        Method that returns a users's credential lists
        Args:
            user_name:name of the user
            user_password:password of the user
        '''

        user_credential_list=[]

        for credential in cls.credential_list:
            if credential.user_name==name   and credential.user_password==password:
                user_credential_list.append(credential)

        return user_credential_list        

    @classmethod
    def generate_password(cls,pass_length):
        '''
        Method that generates a random alphanumeric password for a user
        '''
        #password characters
        pass_chars= string.ascii_letters+string.digits+string.punctuation

        #password
        password=''.join(random.choice(pass_chars) for i in range(pass_length))

        return password

    @classmethod
    def find_by_name(cls,name,password,credential_name):
        '''
        Method that takes a credential name and returns the a credential name that mayches it
        
        Args:
            credential_name:Name of the credential to search for
        Returns:
            The actual credential that matches the name
        '''
        for credential in cls.credential_list:
            if credential.user_name==name   and credential.user_password==password and credential.credential_name==credential_name:
                return credential

    @classmethod
    def credential_exists(cls,name,password,credential_name):
        '''
        Method that takes credential name and returns a boolean if the credential exists
        Arg:
        credential_name:Name of the credential
        user_name:Name of the user who owns the credential
        user_password:Password of the user
        '''

        for credential in cls.credential_list:
            if credential.user_name==name   and credential.user_password==password and credential.credential_name==credential_name:
                return True
  
        return False       




