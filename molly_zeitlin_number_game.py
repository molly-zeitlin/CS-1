import random                                                                                                                           #import random library
name = input("What is your name? ")                                                                                                     #ask user what their name is
print("Good luck", name)                                                                                                                #display good luck with name
while True:                                                                                                                             #create forever loop
        number = random.randint(1, 10)                                                                                                  #computer chooses a random number from 1-10
        guesses = 5                                                                                                                     #set guess to 5
        correct = 0                                                                                                                     #set correct to 0
        rounds = 0                                                                                                                      #set rounds to 0
        while guesses > 0:                                                                                                              #while guess > 0
            while True:                                                                                                                 #create forever loop
                guess = input("Guess a number between 1-10! ")                                                                          #ask user for a number 1-10
                try:                                                                                                                    #try:
                    guess = int(guess)                                                                                                  #computer tries to convert guess to integer good!
                    if guess >= 1 and guess <= 10:                                                                                      #if the guess >= 1 and guess <=10
                        break                                                                                                           #end forever loop
                    else:                                                                                                               #if user responds anything else
                        print("Please enter a number between 1-10! ")                                                                   #ask the user for a number 1-10
                except ValueError:                                                                                                      #except valueError
                        print("Please enter a number between 1-10! ")                                                                   #ask the user for a number 1-10
            if guess == number:                                                                                                         #if the user guesses the computer's number
                print("You got it!")                                                                                                    #display you got it
                correct +=1                                                                                                             #add 1 to variable correct
                break                                                                                                                   #end forever loop
            elif guess > number:                                                                                                        #if user guess is higher than computer's number
                print("Your guess is too high!")                                                                                        #display guess is too high
            else:                                                                                                                       #if user responds anything else
                print("Your guess is too low!")                                                                                         #display guess is too low
            guesses -=1                                                                                                                 #subtract one from guesses

        if guesses == 0:                                                                                                                #if guesses is 0
                ("You lost this round ")                                                                                                #display you lost this round
                rounds +=1                                                                                                              #add one to rounds
        while True:                                                                                                                     #create forever loop
                again = input(f"You have gotten {correct} correct, out of {rounds} rounds. Would you like to play again? y/n: ")        #ask user to play again
                if again == "n":                                                                                                        #user doesnt want to play again
                        exit()                                                                                                          #end code
                elif again == "y":                                                                                                      #user wants to play again
                        break                                                                                                           #end forever loop
                else:                                                                                                                   #if user responds anything else
                        print("Invalid response")                                                                                       #display invalid response



