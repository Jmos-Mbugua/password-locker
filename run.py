#!/usr/bin/env python3.6
from credentials import Password
import sys
from credentials import User
# from termcolor import colored, cprint

def create_credential(sname, fname, lname, password):
    '''
    Function to create a new user credentials
    '''
    new_credential = Password(sname, fname, lname,password)
    return new_credential



def save_credential(credential):
    '''
    Funtion to save the credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(site_name):
    '''
    Function to find a credential
    '''
    return Password.find_by_account_name(site_name)

def check_existing_credentials(account_name):
    '''
    Function to check whether a credential exists
    '''
    return Password.credential_exist(account_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Password.display_credentials()



#Users funtions
def create_user(username, psswrd):
    '''
    Function to create a new user credentials
    '''
    new_user = User(username, psswrd)
    return new_user

def save_users(user):
    '''
    Funtion to save the credential
    '''
    user.save_users()



def main():
    print("Hello, Welcome to Password Locker. What is your name?")
    user_name = input()

    while True:
        print(f"Hello {user_name}, Please use these short codes to either login to your account or sign in. lg - log into your account, ca - create an account")
        s_code = input().lower()

        if s_code == 'ca':
            print("Enter username")
            fusername = input()

            print("Enter password")
            fpin = input()

            save_users(create_user(fusername, fpin))

            print("You have successfully created an account")
            print("Please proceed to log in")

        
        
            print("Enter your username")
            username = input()
            

            print("Enter your password")
            pin = input()

            if username == fusername and pin == fpin:
                print("lOGIN SUCCESSFUL")
                pass
                while True:
                    print("Use these short codes: sc - Save existing credentials, cc - Create new credentials, dc - display credentials, fc - Find a credential, ex-exit the account")

                    short_code = input().lower()

                    if short_code == 'cc':
                        print("New Credentials")
                        print("-"*10)

                        print("Site Name...")
                        sname = input()

                        print("First Name")
                        fname = input()

                        print("Last Name....")
                        lname = input()

                        print("Password")
                        password = input()

                        save_credential(create_credential(sname, fname, lname, password)) #Create and save credentials
                        print('\n')
                        print(f"New Credential {fname} {lname} created")
                        print('\n')

                    elif short_code == 'sc':
                        print("Save Existing credentials")
                        print("-"*10)

                        print("Site Name...")
                        sname = input()

                        print("First Name")
                        fname = input()

                        print("Last Name")
                        lname = input()

                        print("Password")
                        password = input()

                        save_credential(create_credential(sname, fname, lname, password)) #Create and save credentials
                        print('\n')
                        print(f"{sname} credentials saved")
                        print('\n')


                    elif short_code == 'dc':
                        if display_credentials():
                            print("Here is a list of all you credentials")
                            print('\n')

                            for credential in display_credentials():
                                print(f"{credential.account_name} .... {credential.first_name} {credential.last_name} .... {credential.user_password}")
                                print('\n')

                        else:
                            print('\n')
                            print("You don't seem to have any credentials saved yet")
                            print('\n')

                    elif short_code == 'fc':
                        print("Please enter the site name you want to search for")

                        search_site = input()
                        if check_existing_credentials(search_site):
                            search_site = find_credential(search_site)
                            print(f"{search_site.first_name} {search_site.last_name}")
                            print("-"*20)

                            print(f"Password.....{search_site.user_password}")

                        else:
                            print("These credentials do not exist")

                    elif short_code == "ex":
                        print("Bye.....")
                        break
                    else:
                        print("I really didn't get that")
            else:
                print("Invalid login details")

        elif s_code == 'lg':
            print("Please Enter your name")
            inputname = input()

            print("Enter Your Password")
            inputpass = input()

            print("The login details you entered do not seem to exist. Please create an account before you can login")
    

        

    




if __name__ == '__main__':
    
    main()

