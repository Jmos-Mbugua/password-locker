class Password :
    '''
    class that creates instances of users accounts credentials
    '''

    credentials_list = [] #creates an empty list for user credentials

    def __init__(self, account_name, first_name, last_name, user_password):
        self.account_name = account_name
        self.first_name = first_name
        self.last_name = last_name
        self.user_credentials = user_password


