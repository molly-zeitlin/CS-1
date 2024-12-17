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
import time
print("ALARM")
brush_teeth = False
while True:
    snooze = str.lower(input("Snooze? yes/no: "))
    if snooze == "yes":
        print_colored("Sleep for 5 more minutes", "blue")
        time.sleep(5)
    elif snooze == "no":
        print_colored("Get up!", "magenta")
        break
    else:
        print_colored("INVALID RESPONSE", "red")
while True:
    brush_teeth_1 = str.lower(input("Brush teeth now? yes/no: "))

    if brush_teeth_1 == "yes":
        print_colored("Brush teeth!", "white")
        brush_teeth = True
        break
    elif brush_teeth_1 == "no":
        break
    else:
        print_colored("INVALID RESPONSE", "red")
while True:
    get_changed = str.lower(input("Get changed? yes/no: "))
    if get_changed == "yes":
        print_colored("Go to closet and get changed!", "cyan")
        while True:
            eat_breakfast = str.lower(input("Eat breakfast? yes/no: "))
            if eat_breakfast == "yes":
                print_colored("Go downstairs and eat breakfast!", "yellow")
                break
            elif eat_breakfast == "no":
                print_colored("Eat breakfast at school or skip it today!", "yellow")
                break
            else:
                print_colored("INVALID RESPONSE", "red")
        while True:
            if brush_teeth:
                break
            else:
                while True:
                    brush_teeth_now = str.lower(input("Brush teeth? yes/no: "))
                    if brush_teeth_now == "yes":
                        print_colored("Brush teeth!", "white")
                        brush_teeth = True
                        break
                    elif brush_teeth_now == "no":
                        print_colored("Be unhygenic", "orange")
                        break
                    else:
                        print_colored("INVALID RESPONSE", "red")
                break
    elif get_changed == "no":
        print("Go downstairs and eat breakfast!")
        while True:
            get_changed_now = str.lower(input("Get changed? yes/no: "))
            if get_changed_now == "yes":
                print_colored("Go back upstairs and get changed!", "cyan")
                break
            elif get_changed_now == "no":
                print_colored("Don't go to school today", "green")
                quit()
            else:
                print_colored("INVALID RESPONSE", "red")
        while True:
            if brush_teeth:
                break
            else:
                while True:
                    brush_teeth_now_1 = str.lower(input("Brush teeth? yes/no: "))
                    if brush_teeth_now_1 == "yes":
                        print_colored("Brush teeth!", "white")
                        brush_teeth = True
                        break
                    elif brush_teeth_now_1 == "no":
                        print_colored("Be unhygenic", "orange")
                        break
                    else:
                        print.colored("INVALID RESPONSE", "red")
                break
        break
    else:
        print_colored("INVALID RESPONSE", "red")
while True:
    leave_for_school = str.lower(input("Leave for school? yes/no: "))
    if leave_for_school == "yes":
        print_colored("Go to school", "magenta")
        break
    elif leave_for_school == "no":
        print_colored("Don't go to school today", "green")
        break
    else:
        print_colored("INVALID RESPONSE", "red")
