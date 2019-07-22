class User:
    
    '''
    class that generates a new instance of a password user
    __init__ method that helps us to define properitis for our objet
    
    Args:
    '''
    user_list = [] #Empty user list
    
    def __init__(self,name,password):
        
        self.name=name
        self.password=password
        
        
    def save_user(self):
           
        '''
        save_contact method save user objects into user_list
        '''
        User.user_list.append(self)
        
    @classmethod
    def display_users(cls):
        '''
        method that returns users using the password locker
        app
        '''
        return cls.user_list 

     
    @classmethod
    def user_verified(cls,name,password):
    
        '''
        methods that takes the user logings and returs boolean its true
        
        Args:
            name:User name to search
            password:password to match
            
        return:
              Boolean true if they both match to a user and false 
              if it doesn't
        '''
        # for user in cls.user_list:
        #     if user.name==name and user.password==password:
        #         return True
        # return False
          
        
   
    
  
        

        
        
        