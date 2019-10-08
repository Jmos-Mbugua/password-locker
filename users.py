class User:
    '''
    class that creates instances of users
    '''

    users_list = [] #creates an empty list for us


    def __init__(self, user_name, user_passwrd):
        self.user_name = user_name
        self.user_passwrd = user_passwrd

    def save_user(self):
        '''
        This method saves new object to users list
        '''
        User.users_list.append(self)

    # @classmethod
    # def user_authenticate(cls, name, passwrd):
    #     '''
    #     This method checks whether the input details from the user match those in the user_list and returns boolean
    #     '''
    #     for user in cls.users_list:
    #         if user.user_name == name and user.user_passwrd == passwrd:
    #             return True
    #     return False

