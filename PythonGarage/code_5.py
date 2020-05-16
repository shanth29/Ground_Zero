""" 
Desing Health Management system. Take 3 clients as Amit, Nikhil. Sumit.
Each client has two record files one for food and another for Exercise.
Write a function to take client Name and display respective option wheather he wants to Eat or do Exercise.
Add time stamp to the event performed by client.
Also write function to retrieve the specific client data 
"""

import datetime

def get_date():

    """ To Get current Time and Date """
    return datetime.datetime.now()


def get_client(client_name):

    """ To check client and get his choice"""

    client_records = ["amit", "nikhil", "sumit"]
    if client_name.lower() in client_records:
        print(f"\t\t\t\tWelcome {client_name}")
        _option1 = int(input("""\n\t1. For Exercise Press '1',
        2. For Diet Press '2', \n\t\t==> """))
        return _option1
    else:
        print("Entered Person is not Registered")


def get_choice(user_choice):
    if user_choice == 1:
        _type_of_facility = "Exercise"
    elif user_choice == 2:
        _type_of_facility ="Diet"
    else:
        print("Wrong choice")
    print(f"Enter '1' to add to {_type_of_facility} and '2' to view your previous logs regarding {_type_of_facility}")
    _type_of_mode = int(input("===> "))
    response = {_type_of_facility:_type_of_mode}
    return response


def read_file(user_name, user_feeds):
    with open(str(user_name) + str(user_feeds) +".txt", "r") as f1:
        file_content_1 = f1.readlines()
    return file_content_1

def write_file(user_name, _facility, date, content):
    input_contents = str(date) + "|" + str(content)
    print(input_contents)
    with open(str(user_name) + str(_facility) +".txt", "a") as f1:
        file_content_2 = f1.write(input_contents)
    return ("Success")



exit = 0
try:
    while exit == 0:
        print("**************************************************************************************************")
        print("**************************Welcome To Health Management System*************************************")
        print("**************************************************************************************************")

        _date = get_date()
        name_of_client = input("\t\tPlease enter your Name To Login--> ")
        _session = 0
        while _session == 0:
            _choice = get_client(name_of_client)
            get_user_choice = get_choice(_choice)
            for facility, mode in get_user_choice.items():
                if mode == 1 and facility == 'Exercise':
                    input_content = input("Enter the type of exercise you have performed today:")
                    output_of_write = write_file(name_of_client,facility, _date, input_content)
                    print("\t\tEnter 'Yes'/'Y' to continue and 'No'/'N' to Logout")
                    _response1 = input("=====>")
                    if _response1.lower() in "yes":
                        break
                    else:
                        print("You Have Successfully Logged Out")
                        _session = 1
                elif mode == 1 and facility == 'Diet':
                    input_content = input("Enter the type of Diet you had today:")
                    output_of_write = write_file(name_of_client,facility, _date, input_content)
                    print("\t\tEnter 'Yes'/'Y' to continue and 'No'/'N' to Logout")
                    _response1 = input("=====>")
                    if _response1.lower() in "yes":
                        break
                    else:
                        print("You Have Successfully Logged Out")
                        _session = 1
                else:
                    if facility == 'Exercise':
                        file_content = read_file(name_of_client, facility)
                        print(file_content)
                        print("\t\tEnter 'Yes'/'Y' to continue and 'No'/'N' to Logout")
                        _response1 = input("=====>")
                        if _response1.lower() in "yes":
                            break
                        else:
                            print("You Have Successfully Logged Out")
                            _session = 1
                    else:
                        facility = "Diet"
                        file_content = read_file(name_of_client, facility)
                        print(file_content)
                        print("\t\tEnter 'Yes'/'Y' to continue and 'No'/'N' to Logout")
                        _response1 = input("=====>")
                        if _response1.lower() in "yes":
                            break
                        else:
                            print("You Have Successfully Logged Out")
                            _session = 1
        print("\t\tEnter 'Yes'/'Y' to continue and 'No'/'N' to Exit")
        _response = input("=====>")
        if _response.lower() in "yes":
            continue
        elif _response.lower() in "no":
            exit = 1
        else:
            ("Give correct choice to Exit")

except Exception as e:
    print(e)
