#Molly Zeitlin
#Provides the user with the option to select a function
#May 5, 2025
#no bugs
#subtract, multiply, divide, get_initials, resverse_string, replace_character

import random
def chorus():
    '''
    Prepares for next function and prints two statements
    Args:
        None
    Returns:
        print: chorus
    '''
    print("Old MacDonald had a farm")
    print("Ee i ee i o!!")

def sing(animal, sound):
    '''
    Uses the previous function to reduce the print statements needed to “sing” a song
    Args:
        animal (str): the animal
        sound (str): the sound the animal makes
    Returns:
        print: the entire song
    '''
    chorus()
    print(f"And on his farm he had some {animal}")
    print("Ee i ee i oh!!")
    print(f"With a {sound}-{sound} here!")
    print(f"And a {sound}-{sound} there!")
    print(f"Here a {sound}, there a {sound}!")
    print(f"Everywhere a {sound}-{sound}!")
    chorus()

def add(x, y):
    '''
    Takes two numbers and prints their sum
    Args:
        x (int): first number
        y (int): second number
    Returns:
        print: the first number plus the second number
    '''
    print(x+y)

def print_list(array):
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        array (list): list that is printed
    Returns:
        print: each element in list vertically
    '''
    for element in array:
        print(element)

def in_list(element, array):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        element ():
        array (list): 
    Returns:
        Boolean
    '''
    return element in array
    
def is_integer(number):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        number (any): determined if it is an integer
    Returns:
        Boolean: true or false 
    Raises:
        ValueError: if number is not an integer
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False

def get_integers():
    '''
    Takes any parameter and returns a boolean based on if it is an integer - uses the previous function to determine if input is an integer
    Args:
        none
    Returns:
        the users' integers
    '''
    while True:
        a = input("Enter number: ")
        b = input("Enter second number: ")

        if is_integer(a) and is_integer(b):
            return int(a), int(b)

def get_random(a,b):
    '''
    Uses get_integers and prints a random number between the two given integers
    Args:
        a (int): first number derived from get_integers
        b (int): second number derived from get_integers
    Returns:
        print: a randomly selected number between the two numbers
    '''
    number = random.randint(a,b)
    print(number)

def count_vowels(word):
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        word (str): the string that its number of vowels are being determined 
    Returns:
        print: number of vowels in the string
    '''
    vowel_count = 0
    for character in word:
        if character in ["a","e","i","o","u","A","E","I","O","U"]:
            vowel_count += 1
    return vowel_count

def subtract(x,y):
    '''
    Takes two integers and prints the difference
    Args:
        x (int): first number
        y (int): second number
    Returns:
        print: difference of the two integers
    '''
    print(x-y)  

def multiply(x,y):
    '''
    Takes two integers and prints the product
    Args:
        x (int): first number
        y (int): second number
    Returns:
        print: the product of the two integers
    '''
    print(x*y)

def divide(x,y):
    '''
    Takes two integers and prints the quotient
    Args:
        x (int): first number
        y (int): second number
    Returns:
        print: the quotients of the two integers
    '''
    print(x/y)

def get_initials(First, Last):
    '''
    Takes a name, prints and returns the initials
    Args:
        First (str): the first name
        Last (str): the last name
    Returns:
        print: the initials of the name
        return: the initials of the name
    '''
    firstI = list(First)
    lastI = list(Last)
    print(firstI[0],lastI[0])
    return(firstI[0],lastI[0])

def reverse_string(string):
    '''
    Takes a string and reverses it
    Args:
        string (str): the string that will be reversed
    Returns:
        print: the reversed string
    '''
    reversed_string = string[::-1]
    print(reversed_string)

def replace_character(string, old, new):
    '''
    Takes a string, an old character, and a new character, and replaces every instance in the string of the old character with the new
    Args:
        string (str): original string
        old (str): original character
        new (str): new character
    Returns:
        print: the new string
    '''
    new_string = string.replace(old, new)
    print(new_string)

def main():
    while True:
            option = input('What would you like to do? 1. Sing a song, 2. Add two integers, 3. Print each element in a list individually, 4. Determine if an element is in a list, 5. Determines if any parameter is an integer, 6. Provide the computer with two parameters to determine if they are integers, 7. Print a random number between the two given numbers, 8. Determine the number of vowels in a string, 9. Subtract two integers, 10. Multiply two integers, 11. Divide two integers, 12. Print the initials of a name, 13. Reverse a string, or 14. Replace every form of one character in a string with another (Respond with the corresponding number or STOP): ')
            if option == "1":
                sing("cows", "moo")
                sing("chicks", "cluck")
                sing("pigs", "oink")
            elif option == "2":
                add(5, 3)
            elif option == "3":
                countries = ["Italy", "France", "England"]
                print_list(countries)
            elif option == "4":
                colors = ["red", "purple", "blue", "yellow"]
                in_list("red", colors)
            elif option == "5":
                is_integer("word")
            elif option == "6":
                a, b = get_integers()
            elif option == "7":
                a, b = get_integers()
                get_random(a,b)
            elif option == "8":
                print(count_vowels("computer"))
            elif option == "9":
                subtract(10, 2)
            elif option == "10":
                multiply(6, 4)
            elif option == "11":
                divide(9, 3)
            elif option == "12":
                get_initials("Talia", "Sandhu")
            elif option == "13":
                word = input("Enter a string: ")
                reverse_string(word)
            elif option == "14":
                word = input("Enter a string: ")
                c_old = input("Enter a character in your string: ")
                c_new = input("Enter a different character: ")
                replace_character(word, c_old, c_new)
            elif option == "STOP":
                break
            else:
                print("INVALID RESPONSE!!")

main()
