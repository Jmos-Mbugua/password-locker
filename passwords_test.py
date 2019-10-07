import unittest
from passwords import Password

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the Password class behaviours
    '''

    def setUp(self):
        # self.new_credentials = Password("Facebook", "John","Mbugua", "jmos849") #Create user credential object
        
        
        self.new_credentials = Password("Facebook","John","Mbugua","jmos849")

    def test__init(self):
        '''
        Test to check whether the credentials objects are instantiated correctly
        '''
        self.assertEqual(self.new_credentials.account_name,"Facebook")
        self.assertEqual(self.new_credentials.first_name,"John")
        self.assertEqual(self.new_credentials.last_name,"Mbugua")
        self.assertEqual(self.new_credentials.user_password,"jmos849")

    def test_save_credential(self):
        '''
        Test to check if the object is saved into the credentials list
        '''
        self.new_credentials.save_credential()
        self.assertEqual(len(Password.credentials_list),1)

    def test_save_multiple_credentials(self):
        


if __name__ == '__main__':
    unittest.main()
        


    

