#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(name, password,):
    """
    function to create a new user
    """
    new_user = User(name, password,)
    return new_user


def save_user(user):
     """
     function to save the new user
     """
     user.save_user()


def create_credential(user_name, user_password,):
    """
    function to create new user credentials
    """
    new_credential = Credential(user_name, user_password,)
    return new_credential


def save_credential(credential):
    """
    function to safe user credentials
    """
    credential.save_credential()


def display_users():
    '''
    Function that returns the users using pass_locker
    '''
    return User.display_users()


def user_log_in(name, password,):
    '''
    Function that allows a user to log in to their credentials
    '''
    verified_user = User.user_verified(name, password,)

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
    '''
    Function that generate a random password for a user's credential
    Args:
        pass_length:Length the user wants the password to be
    '''
    password = Credential.generate_password(pass_length)

    return password


def display_credentials(user_name, user_password,):
    '''
    Function that returns all the users saved credentials
    '''

    return Credential.display_credential(user_name, user_password, email)


def find_by_name(user_name, user_password,credential_name):
    '''
    Function that find a credential by name and returns the credential
    '''

    return Credential.find_by_name(user_name, user_password,credential_name)


def main():

    print("Welcome to your Password Locker, choose your path from the list of allowed actions")

    while True:
            print('''Use these short codes to get around \n
            ShortCodes: \n
                ca:create new pass locker account \n
                du:display users using pass locker\n
                lg:login to your account \n
                ex:exit the app          ''')
        #take user input
            short_code = input().lower()

            if short_code == "ca":
                print("-"*27)
                print("New Password Locker Account")
                print("-"*27)
                print("\n")

                print("Enter User Name")
                user_name = input()

                print("Enter Account Password")
                user_password = input()


                save_user( create_user(user_name,user_password) ) #create and save user
                print('\n')
                print(f"Password Locker Account for {user_name} created succesfully!!")
                print('\n')
            
            elif short_code == 'du':
                '''
                Displays name of current users
                '''
                if display_users():
                    print("Here are the users using password locker")
                    print('-'*30)
                    print('\n')   

                    for user in display_users():
                        print(f"User_Name:{user.name}")
                        print("\n")

                else:
                    print('\n')
                    print("**Password locker has no users!\n   Fancy being first user?**")
                    print('\n')


            elif short_code == "lg":
                '''
                Logs in user to the password locker account
                '''
                print('\n')
                print("*"*35)    
                print("Log into Password Locker Account")
                print("*"*35)

                print("Enter User Name")
                user_name = input()
                
                print("Enter Password")
                user_password = input()
                
                print("Enter email")
                user_email = input()


                if  user_log_in(user_name,user_password):
                    print('\n')
                    print("*"*40)    
                    print(f"Welcome {user_name} to your Credentials" )
                    print("*"*40)

                while True:
                    '''
                    Loop to run functionalities after successful login
                    '''
                    print('''Use these short code to navigate \n
                        cc:Create a new credential \n
                        dc:Display saved credentials \n
                        gc:Generate credential with a random password\n
                        dl:Delete credential\n    
                        ex:Log out of credential account           ''')

                    #get short code from user
                    short_code = input().lower()

                    if short_code == "cc":
                        '''
                        Creating a credential
                        '''
                        print('\n')
                        print("New Credential")
                        print("-"*15)

                        print("Name of the Credential...")   
                        credential_name = input()

                        print("Password of the Credential...")
                        credential_password = input()

                        #create and save credential
                        save_credential( create_credential(user_name,user_password,credential_name,credential_password)
                        )

                        print('\n')
                        print(f"Credentials for *{credential_name}* has been created and saved successfully")
                        print('\n') 

                    elif short_code == 'dc':
                        '''
                        Returning the user's saved credentials
                        '''

                        if display_credentials(user_name,user_password):
                            print('\n')
                            print(f"{user_name} Credentials")
                            print("-"*25)

                            for credential in display_credentials(user_name,user_password):
                                print(f"Account:{credential.credential_name}")
                                print(f"Password:{credential.credential_password}")  
                                print('-'*25)

                        else:
                            print("\n")
                            print("You have no credentials saved")
                            print("Create a new one...")
                            print("\n") 

                    elif short_code == 'gc':
                        '''
                        Generate Credential with a randomised password
                        '''
                        print("\n")
                        print("New Credential With Auto-Generated Password")
                        print("-"*42)
                        print("\n")

                        print("Enter Name of Credential...")
                        credential_name = input()

                        print("Enter length size for the password e.g 7")
                        pass_length = int(input())

                        #create,save new credential with a randomised key
                        save_credential(create_credential(user_name,user_password,credential_name,(generated_password(pass_length))))  

                        print('\n')
                        print(f"**Credential {credential_name} has been created and saved successfully**")
                        print('\n')    

                    elif short_code == 'dl':
                        '''
                        Delete a Credential
                        '''
                        print('\n')
                        print("Enter Name Of The Credential...")
                        print("-"*31)
                        credential_name = input()

                        if credential_exists(user_name,user_password,credential_name):
                            search_credential = find_by_name(user_name,user_password,credential_name)
                            print(f"{search_credential.credential_name}\n{search_credential.credential_password}")

                            print('\n')
                            print(f"Are You Sure You Wish to Delete {search_credential.credential_name}? \n   This Action is Irreversible")    
                            print("Enter y/n...")
                            print('\n')

                            delete_response = input().lower()

                            if delete_response == 'y':
                                search_credential.delete_credential()
                                print("**Credential Deleted Successfully**")
                                print('\n')

                            else :
                                print("Probably a good idea")
                                print("... Exiting delete action")
                                print("\n")
                                    

                        else:
                            print(f"**No credential with the name {credential_name} exists**")
                            print("\n")
                            


                    elif short_code == 'ex':
                        '''
                        Exit credential account
                        '''
                        print(f"See you later {user_name}")
                        print("Logging Out...")
                        print("Logged Out")
                        print('\n')
                        break 
                    else:
                        '''
                        User types wrong code
                        '''
                        print('\n')
                        print(f"Sorry there is no option associated with code:{short_code}")  
                        print("Try Again..!")
                        print('\n')  


            else:
                print('\n')
                print(f"No Account for {user_name}")
                print("Please try again or create an account")
                print('\n')

           
          
                        
if __name__ == "__main__":
    main()
    
