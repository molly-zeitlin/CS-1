import random
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
def input_colored(text, color):                                                             
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
    input(color_codes.get(color, "") + text + color_codes["reset"])
while True:
    random_color = random.choice(["green", "yellow", "blue", "magenta", "cyan", "white", "red"])
    question = input_colored("Ask Magic 8 Ball a Question!", random_color)
    random_response = random.choice(["Yes!", "No!", "Maybe!", "Ask again later!"])
    print_colored(random_response, random_color)
