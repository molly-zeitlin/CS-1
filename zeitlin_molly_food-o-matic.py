#Molly Zeitlin
#randomly generating meals for user
#4/4/2025
#no bugs
#incorporated colors, customized menu, customized prices, and ensures that user enters a valid number
#https://www.w3schools.com/python/python_try_except.asp

import random
#import random library
def print_colored(text, color):
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    print(color_codes.get(color, "") + text + color_codes["reset"])
mains = ['burger', 'pizza', 'buffalo wings', 'chicken fingers', 'grilled chicken', 'grilled cheese', 'salmon', 'steak', 'steak tacos']
#create list of main course menu items
m_prices = [20,15,25,18,25,15,30,30,20]
#create list of main course menu item prices
flairs = ['with fries', 'with tater tots', 'with baguette', 'with potatoes', 'with salad', 'with chips and salsa', 'with steamed vegetables', 'with tomato soup', 'with rice']
#create list of side dish menu items
f_prices = [1,1,2,1,3,3,5,2,1]
#create list of side dish menu item prices
while True:
#create forever loop
    try:
    #continue with code unless ValueError occurs
        while True:
        #create forever loop
            items = int(input("How many menu items do you need? "))
            #user's response lies in variable
            if items < 10:
            #if user responds number less than 10
                break
                #end forever loop
            else:
            #if user responds any other number
                print_colored("Please enter a number less than 10!", "red")
                #display message in red
        for i in range(items):
        #create for loop
            random_colored = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
            #computer randomly selects color from list
            main = random.choice(mains)
            #computer randomly selects main course from list
            index = mains.index(main)
            #identify index of random main course choice
            flair = random.choice(flairs)
            #computer randomly selects side dish from list
            index2 = flairs.index(flair)
            #identify index of random side dish choice
            price = m_prices[index] + f_prices[index2]
            #add prices of randomly selected meals
            print_colored(f"{main} {flair}, ${price}", f"{random_colored}")
            #display message in randomly selected color
        break
        #end forever loop
    except ValueError:
    #if user response is not a number
        print_colored("Please enter a number! ", "red")
        #display message in red