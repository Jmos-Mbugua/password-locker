class Password :
    '''
    class that creates instances of users accounts credentials
    '''

    credentials_list = [] #creates an empty list for user credentials

    def save_credential(self):
        '''
        Method to save a new object in the credential list
        '''
        Password.credentials_list.append(self)

    def delete_credential(self):
        '''
        Method to delete a credential from the list
        '''
        Password.credentials_list.remove(self)

    

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method that takes in a site name and returns the credentials
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credential actually exists
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True

        return False


    @classmethod
    def display_credentials(cls):
        '''
        Method that displays the credentials list
        '''
        return cls.credentials_list



    def __init__(self, account_name, first_name, last_name, user_password):
        self.account_name = account_name
        self.first_name = first_name
        self.last_name = last_name
        self.user_password = user_password










    


