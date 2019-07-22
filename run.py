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
    # Dealing user class first
    print("Hello! Welcome to Password Locker! Please Key in your name:  ")
    name = input ()
    print(f"Hey {name}, please create an account to access Password Locker")
    print('\n')
    
    print("Reply with these short codes : ca - create account,  ex -exit ")
    
    

    while True:
        short_code = input().lower()

        if short_code == 'cc':
            
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()
            
            print("\n")

            print("Password: ")
            password = input()

            save_user(create_useraccount(username, password))
            print('\n')
            print(f"{name}'s Account : ")
            print(f"Username: {username} \n , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            
          
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit t")
            

        elif short_code == "ca":
            print("Enter account details: ")
  
            account = input()
            print("Email: ")
            email = input()
        
            print("Would you like a generate password?")
            res = input()
            if res =="yes":
                letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)            
                passlock = "".join(random.sample(letters,8))
                print(f"Your password has 8 characters ")
                print(passlock)
                save_cred(create_credentials(account, email, passlock))
                print("Credentials saved! Enter 'da' to see account")
              
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                
            elif res == "no":
                print("Password: ")
                passlock = input()   
                save_cred(create_credentials(account, email, passlock))
                print("Credentials saved! Enter 'da' to see account")
                
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                
            else:
                print("i dont get it please use shortcode 'ca' and start again")

        elif short_code == "da":
            print(f"These are your accounts {name}:")
            
            for cred in display_cred():
                print(f"{cred.account} {cred.email} {cred.passlock}")
            else:
                
                print("If empty, you do not have any accounts saved")

        elif short_code == "fa":
      
            search_cred= input()
            if find_account(search_cred):
                search_acc = find_account(search_cred)
                print(f"{search_acc.account} {search_acc.email} { search_acc.passlock}")
            else: print("This account does not exist")
            
        elif short_code == "gp":
                letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                
            
        elif short_code == 'ex':
    
            print("logging out...")
            print('\n')
            print('\n')
            print("logged out")
    
            break


        else:
            print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")

if __name__ == '__main__':
    main()  

