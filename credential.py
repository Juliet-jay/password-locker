class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_list = []

    def __init__(self, user, password, email):
        self.user = user
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_credential method saves credential objects into credential_list
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list

