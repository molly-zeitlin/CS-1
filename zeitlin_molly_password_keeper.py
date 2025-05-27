#Molly Zeitlin
#Stores and returns all the usernames and passwords for corresponding websites
#May 19, 2025
#no bugs
#Allow the user to retroactively add more usernames and passwords, Allow the user to change usernames and passwords, Store the list of websites with usernames and passwords in an excel spreadsheet, Clear screen, Require a password to enter the password keeper, Generate a secure password for the user, Check how complex/secure the passwords are

import csv
import random
import time
import os

def add_entry(websites, usernames, passwords):
    '''
    Allows user to store website with corresponding username and password.
    Args:
        websites (list): list of all stored websites
        usernames (list): list of all stored usernames
        passwords (list): list of all stored passwords
    Returns:
        adds information into lists
    '''
    website = input("Please enter a website: ")
    websites.append(website)
    username = input("Please enter the corresponding username: ")
    usernames.append(username)
    password = input("Please enter the corresponding password (press 'g' to generate): ")

    if password.lower() == "g":
        password = generate_password()
    passwords.append(password)

def print_entry(website, username, password):
    '''
    Allows the user to print their stored information (a specific website and its corresponding username and password)
    Args:
        website (str): a specific element from the website list
        username (str): a specific element from the username list
        password (str): a specific element from the password list
    Returns:
        print: the website element with the corresponding username and password
    '''
    print(f'''
Website: {website}
Username: {username}
Password: {password}
        ''')

def print_entries(websites, usernames, passwords):
    '''
    Allow user to print all of their stored information.
    Args:
        websites (list): list of all stored websites
        usernames (list): list of all stored usernames
        passwords (list): list of all stored passwords
    Returns:
        print: all the websites, usernames, and passwords - organized by index
    '''
    for i in range(len(websites)):
        print_entry(websites[i], usernames[i], passwords[i])

def get_website(websites):
    '''
    Obtain the index of the user's desired website.
    Args:
        websites (list): list of all stored websites
    Returns:
        index of an element from the website list
    '''
    while True:
        website = input("Enter a website: ")

        if website in websites:
           return websites.index(website)
        else:
            print("INVALID RESPONSE")

def change_info(array, websites, element):
    '''
    Allow the user to alter the information stored in password keeper
    Args:
        array (list): list of information where the change is occurring
        websites (list): list of all stored websites
        element (str): single form of the list where the change is occurring
    Returns:
        new information that replaces an old username or password
    '''
    index = get_website(websites)
    array[index] = input(f"Enter your new {element}: ")

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.
    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])
    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)

def get_password_length():
    '''
    Get length of a password
    Returns:
        print: 
    '''
    while True:
        try:
            length = int(input('Enter secure password length: '))
            
            if length < 4:
                print("Length should be at least 4")
                continue
            return length
        except ValueError:
            print("Not an integer!")

def generate_password():
    '''
    Uses "check_security" function to generate a new secure password
    Returns:
        newly generated secure password
    '''
    characters = list("abcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?")
    length = get_password_length()
    while True:
        pwd = ''.join(random.sample(characters, length))
        
        if check_security(pwd, length, False):
            return pwd
        
def check_security(pwd, length, display):
    '''
    Check how complex/secure the passwords are
    Args:
        pwd (str): the password that the security is being checked
        length (int): the minimum length the password should be
        display (boolean): determines whether or not to print if password is secure
    Returns:
        Boolean
        print: password is not secure
        print: password is secure
    '''
    if len(pwd) < length or pwd.lower() == pwd or pwd.upper() == pwd or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list("!@#$%^&*?")):
        if display:
            print(f"{pwd} is not secure")
        return True
    else:
        if display:
            print(f"{pwd} is secure")
        return False

def clear_console(wait):
    '''
    Clear the console
    Args:
        wait (int): time in seconds to pause before continuing with program
    '''
    time.sleep(wait)
    os.system("cls")

def login(code, tries):
    '''
    Requires the user to enter their secret code to get into the password keeper
    Args:
        code (str): the user's secret code
        tries (int): the number of tries the user has to enter the correct code - or else they are banned
    Return:
        print: you are in the password keeper 
        print: you are wrong
        print: you are banned
    '''
    for i in range(tries):
        pwd = input("Enter the secret code: ")

        if pwd == code:
            print("You're in!")
            clear_console(2)
            return True
        else:
            print(f"You're wrong - you only have {tries-i-1} tries left!")
    print("YOU'RE BANNED")
    clear_console(2)
    exit()

def main():
    websites = []
    usernames = []
    passwords = []
    secret_code = input("Create a password to enter the password keeper: ")
    add_entry(websites, usernames, passwords)
    clear_console(2)
    login(secret_code, 3)

    while True:
        clear_console(2)
        extra_entry = input('''
Would you like to save another website (with the corresponding username and password)?
Please enter repeat or STOP: ''').lower()
        if extra_entry == "repeat":
            add_entry(websites, usernames, passwords)
        elif extra_entry == "stop":
            print('''
1. Print a list of your websites - along with the corosponding usernames and passwords
2. Access a specific website's username and password
3. Change one of your usernames or passwords
4. Export list of websites with usernames and passwords to a csv
5. Generate a new secure password
6. Check security of a password''')
            user_choice = input("Please enter a number from one of the options listed above (or 'q' to quit): ").lower()

            if user_choice == "q":
                exit()
            elif user_choice == "1":
                print_entries(websites, usernames, passwords)
            elif user_choice == "2":
                i = get_website(websites)
                print_entry(websites[i], usernames[i], passwords[i])
            elif user_choice == "3":
                while True:
                    element = input("Please enter username, password, or STOP: ").lower()
                    if element == "username":
                        change_info(usernames, websites, element)
                    elif element == "password":
                        change_info(passwords, websites, element)
                    elif element == "stop":
                        break
                    else:
                        print("INVALID RESPONSE")
            elif user_choice == "4":
                filename = input("Enter the name of your csv file: ")
                export_to_csv(filename+".csv", ["Websites", "Usernames", "Passwords"], websites, usernames, passwords)
            elif user_choice == "5":
                print(f'Generated password: {generate_password()}')
            elif user_choice == "6":
                pwd = input('Enter password to check: ')
                length = get_password_length()
                check_security(pwd, length, True)
            else:
                print("INVALID RESPONSE")

main()