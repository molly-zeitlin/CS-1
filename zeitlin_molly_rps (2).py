#cat                                                                                                                                                                                 #extra credit
import random                                                                                                                                                                        #import random library                                                                                                                                              
import os                                                                                                                                                                            #import os library
def colored_text(text, color, input_or_print):                                                                                                                                       #create function of importing color for either input or print                                                                                       
    color_codes = {
        "red": "\033[91m",                                                                                                                                                           #link color with color values
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    if input_or_print == "print":                                                                                                                                                    #if colored text is printed
        print(color_codes.get(color, "") + text + color_codes["reset"])                                                                                                              #print in color
    else:                                                                                                                                                                            #if colored text is used for anything else
        return input(color_codes.get(color, "") + text + color_codes["reset"])                                                                                                       #print question in color (for input), user response lies in variable 
while True:                                                                                                                                                                          #create forever loop
    user_choice = str.lower(input("Welcome! Would you like to play Rock, Paper, Scissors? Or ask the Magic 8 a question? Respond rps/m8b/quit: "))                                   #print question, user response lies in variable
    
    if user_choice == "quit":                                                                                                                                                        #if user responds "quit"
        break                                                                                                                                                                        #end forever loop
    elif user_choice == "rps":                                                                                                                                                       #if user responds rps
        while True:                                                                                                                                                                  #create forever loop
            user_decision = str.lower(input("Would you like to play multiplayer or against the computer? Respond m/c: "))                                                            #print question, user response lies in variable
            user1_name = input("Player 1, enter your name: ")                                                                                                                        #print question, user response lies in variable

            if user_decision == "c":                                                                                                                                                 #if user responds "c"
                user2_name = "bot"                                                                                                                                                   #set variable to "bot"
                break                                                                                                                                                                #end forever loop
            elif user_decision == "m":                                                                                                                                               #if user responds "m"
                user2_name = input("Player 2, enter your name: ")                                                                                                                    #print question, user response lies in variable
                break                                                                                                                                                                #end forever loop
            else:                                                                                                                                                                    #if user responds anything else
                colored_text("INVALID RESPONSE", "red", "print")                                                                                                                     #print message in red

        score = 0                                                                                                                                                                    #set variable to 0
        score2 = 0                                                                                                                                                                   #set variable to 0
        score_limit = 3                                                                                                                                                              #set variable to 3

        while True:                                                                                                                                                                  #create forever loop
            user_decision2 = str.lower(input("Would you like to play regluar or a special mode? Respond r/s: "))                                                                     #print question, user response lies in variable
            
            if user_decision2 == "s":                                                                                                                                                #if user responds "s"
                while True:                                                                                                                                                          #create forever loop
                    possible_new = str.lower(input("Would you like to create your own weapon or use the computer's secret weapon? Respond me/comp: "))                               #print question, user response lies in variable
                    
                    if possible_new == "comp":                                                                                                                                       #if user responds "comp"
                        RPS = ["rock", "paper", "scissors", "water"]                                                                                                                 #create list
                        wins = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper"), ("water", "paper"), ("rock", "water"), ("scissors", "water")]                        #create list
                        break                                                                                                                                                        #end forever loop
                    elif possible_new == "me":                                                                                                                                       #if user responds "me"
                        new = str.lower(input("State weapon name: "))                                                                                                                #print question, user response lies in variable
                        RPS = ["rock", "paper", "scissors", new]                                                                                                                     #create list
                        wins = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper"), ("paper", new), (new, "rock"), (new, "scissors")]                                    #create list
                        break                                                                                                                                                        #end forever loop
                    else:                                                                                                                                                            #if user responds anything else
                        colored_text("INVALID RESPONSE!", "red", "print")                                                                                                            #print message in color
                break                                                                                                                                                                #end forever loop
            elif user_decision2 == "r":                                                                                                                                              #if user responds "r"
                RPS = ["rock", "paper", "scissors"]                                                                                                                                  #create list
                wins = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]                                                                                              #create list
                break                                                                                                                                                                #end forever loop
            else:                                                                                                                                                                    #if user responds anything else
                colored_text("INVALID RESPONSE!", "red", "print")                                                                                                                    #print message in color
        while score < score_limit and score2 < score_limit:                                                                                                                          #create loop with a condition
            user1_response = str.lower(input(f"{user1_name}! {', '.join(RPS).title()}? Choose one! Or quit. "))                                                                      #print question, user response lies in variable
    
            if user_decision == "c":                                                                                                                                                 #if user responds "c"
                user2_response = random.choice(RPS)                                                                                                                                  #set variable to random choice from list
            else:                                                                                                                                                                    #if user responds anything else
                os.system('cls')                                                                                                                                                     #clear page
                user2_response = str.lower(input(f"{user2_name}! Rock, Paper, Scissors, and Water! Choose one! Or quit. "))                                                          #print question, user response lies in variable
                os.system('cls')                                                                                                                                                     #clear page

            if user1_response == "quit" or user2_response == "quit":                                                                                                                 #if both users respond "quit"
                colored_text("Goodbye!", "yellow", "print")                                                                                                                          #print message in color
                colored_text(f"{user1_name} = {score} and {user2_name} = {score2}", "magenta", "print")                                                                              #print message in color
                break                                                                                                                                                                #end forever loop
            elif (user1_response, user2_response) in wins:                                                                                                                           #if user one wins
                colored_text(f"{user1_name} chose {user1_response} and beat {user2_name} who chose {user2_response}", "white", "print")                                              #print message in color
                colored_text(f"{user1_name} won!", "blue", "print")                                                                                                                  #print message in color
                score +=1                                                                                                                                                            #set variable to 1 higher than before
                score2 -=1                                                                                                                                                           #set variable to 1 lower than before
                colored_text(f"{user1_name} = {score} and {user2_name} = {score2}", "magenta", "print")                                                                              #print message in color
            elif (user2_response, user1_response) in wins:                                                                                                                           #if user two wins
                colored_text(f"{user2_name} chose {user2_response} and beat {user1_name} who chose {user1_response}", "white", "print")                                              #print message in color
                colored_text(f"{user2_name} won!", "blue", "print")                                                                                                                  #print message in color
                score2 +=1                                                                                                                                                           #set variable to 1 higher than before
                score -=1                                                                                                                                                            #set variable to 1 lower than before
                colored_text(f"{user1_name} = {score} and {user2_name} = {score2}", "magenta", "print")                                                                              #print message in color
            elif user1_response == user2_response:                                                                                                                                   #if users respond the same
                colored_text(f"{user1_name} chose {user1_response} and tied with {user2_name} who chose {user2_response}", "white", "print")                                         #print message in color
                colored_text("You tied...Try again!", "green", "print")                                                                                                              #print message in color
            else:                                                                                                                                                                    #if user responds anything else
                colored_text("INVALID RESPONSE!", "red", "print")                                                                                                                    #print message in color
    elif user_choice == "m8b":                                                                                                                                                       #if user responds "m8b"
        while True:                                                                                                                                                                  #create forever loop
            random_color = random.choice(["green", "yellow", "blue", "magenta", "cyan", "white", "red"])                                                                             #create list and set variable to random choice in list
            question = str.lower(colored_text("Ask Magic 8 Ball a Question! Or quit. ", random_color, "input"))                                                                      #print question, user response lies in variable
            if question == "quit":                                                                                                                                                   #if user responds "quit"
                break                                                                                                                                                                #end forever loop
            else:                                                                                                                                                                    #if user responds anything else
                random_response = random.choice(["Yes!", "No!", "Maybe!", "Ask again later!"])                                                                                       #select random list item
                colored_text(random_response, random_color, "print")                                                                                                                 #print random item in random color
    else:                                                                                                                                                                            #if user responds anything else
        colored_text("INVALID RESPONSE!", "red", "print")                                                                                                                            #print message in color