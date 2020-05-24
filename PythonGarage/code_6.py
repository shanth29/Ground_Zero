""" 
SNAKE, WATER and GUN GAME.
"""


import random

def winner_condition(comp, user):
    if comp == "Snake" and user == "Snake":
        return "Tie"
    elif comp == "Water" and user == "Water":
        return "Tie"
    elif comp == "Gun" and user == "Gun":
        return "Tie"

    elif comp == "Snake" and user == "Water":
        return "Comp won"
    elif comp == "Snake" and user == "Gun":
        return "User Won"
    elif comp == "Water" and user == "Gun":
        return "Comp Won"

    elif user == "Snake" and comp == "Water":
        return "User won"
    elif user == "Snake" and comp == "Gun":
        return "Comp Won"
    elif user == "Water" and comp == "Gun":
        return "User Won"


count = sssss0
user_count = 1
comp_count = 1
tie_count = 1
print("\t\t\t##################################################################")
print("\t\t\t\tWelcome TO 'Snake', 'Water', and 'Gun' Game")
print("\t\t\t##################################################################")
try:
    while count < 10:
        _arteffects = ["Snake","Water","Gun"]
        print(f"\n\t\t  Your are Playing Set no.{count} of 10 set Game")
        comp_turn = random.choice(_arteffects)
        
        print("""\n\t\tComputer has chosen its Arteffect, It's Your Turn to Choose:
                    Press 1 for 'Snake', 2 for 'Water', 3 for 'GUN'""")
        user_turn = input("\n\t\t)===>")
        if user_turn.isnumeric() and user_turn != "":
            if user_turn ==  "1":
                user_turn = "Snake"
                output = winner_condition(comp_turn, user_turn)
                print("\t_________________________________")
                print(f"\t\t",output)
                print("\t_________________________________")
                if output == "Tie":
                    tie_count += 1
                elif output == "User Won":
                    user_count += 1
                elif output == "Comp Won":
                    comp_count += 1
            elif user_turn ==  "2":
                user_turn = "Water"
                output = winner_condition(comp_turn, user_turn)
                print("\t_________________________________")
                print(f"\t\t",output)
                print("\t_________________________________")
                if output == "Tie":
                    tie_count += 1
                elif output == "User Won":
                    user_count += 1
                elif output == "Comp Won":
                    comp_count += 1
            elif user_turn ==  "3":
                user_turn = "Gun"
                output = winner_condition(comp_turn, user_turn)
                print("\t_________________________________")
                print(f"\t\t",output)
                print("\t_________________________________")
                if output == "Tie":
                    tie_count += 1
                elif output == "User Won":
                    user_count += 1
                elif output == "Comp Won":
                    comp_count += 1
            else:
                pass

        count += 1
    print(f"Total set Played {count}. Number of set won by Computer is {comp_count}, by user is {user_count} and Tie count is {tie_count}")
    print("Hence winner of this Game is User") if user_count > comp_count else print("Computer is winner of this Game")
except Exception as e:
    print(e)