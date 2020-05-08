""" 
Write a simple code to fetch value from dictionary as output response for given input from user.
"""

my_dict = {"INDIA":"NEW DELHI","UK":"LONDON","SPAIN":"MADRID","RUSSIA":"MOSCOW","JAPAN":"TOKYO", "GERMANY":"BERLIN"}

try:
    while True:
        user_input = input("Please Enter Country Name To Know Its Capital :")
        if user_input == "":
            continue
        else:
            if user_input.upper() in my_dict.keys():
                print(f"Capital of {user_input.upper()} is", my_dict.get(user_input.upper()))
                break
            else:
                print("Search is out of Scope, Please enter correct Input Value")
except:
    print("Please reload and run the program with appropriate input")