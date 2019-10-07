#!/usr/bin/env python3.6
from credentials import Password

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


def main():
    print("Hello, Welcome to Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}, What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: cc - Create new credentials, dc - display credentials, fc - Find a credential, ex-exit the account")

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

                print()




if __name__ == '__main__':
    
    main()

