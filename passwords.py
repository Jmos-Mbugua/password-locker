class Password :
    '''
    class that creates instances of users accounts credentials
    '''

    credentials_list = [] #creates an empty list for user credentials

    def save_credential(self):
        '''
        Test Case to check if the credentials object is saved in the credential list
        '''
        Password.credentials_list.append(self)


    def __init__(self, account_name, first_name, last_name, user_password):
        self.account_name = account_name
        self.first_name = first_name
        self.last_name = last_name
        self.user_password = user_password

    


