import unittest

class Passwords :
    '''
    class that creates instnces of users accounts passwords
    '''

    credentials_list = [] #creates an empty list for user credentials
    
    def __init__(self, first_name, last_name, user_credentials):
        self.first_name = first_name
        self.last_name = last_name
        self.user_credentials = user_credentials


