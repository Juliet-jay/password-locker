from user import User
from credential import Credential


def create_user(name,password,email):
    """
    function to create a new user
    """
    new_user = User(name,password,email)
    return new_user

def save_user(user):
     """
     function to save the new user 
     """
     user.save_user()
     
def create_credential(user_name,user_password,email):
    """
    function to create new user credentials
    """
    new_credential = Credential(user_name,user_password,email)
    return new_credential

def save_credential(credential):
    """
    function to safe user credentials
    """
    credential.save_credential() 

    
    
    

def user_log_in(name,password,email):
    '''
    Function that allows a user to log in to their    credential account
    Args:
        name:Name of the user who created the acount
        password:Password the user used to create the account
    '''
    verified_user=User.user_verified(name,password,email)
    
    return verified_user
       
def del_user(user):
    """
    function to delete a user
    """
    user.delete_user()
    
def del_credential(credential):
    """
    function to delete all users credentials
    """
    credential.delete_credential()
    
def generated_password(pass_length):
    """
    function that generate a random password for a user's credential
    
    Args:
        pass_length:length the user wants the password to be
    """
    # password=Credential.generate_password(pass_length)

    
    



    
       