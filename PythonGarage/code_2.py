""" 
Write a program to accept user's age and print respective message "Your are eligible to Drive" if input age is greater then 18,
if age is less 18 than pop message "Your are not eligible to Drive and tell user by how many year he/she is falling short
and if user enter 18 as input call him for in person review process
"""

try:
    while True:
        user_age = input("Please Enter your current age :")
        if user_age != "" and user_age.isnumeric():
            user_age = int(user_age)
            if user_age >=10 and user_age >18 and user_age <=70:
                print(f"User's present age is {user_age} and he is eligible to Drive")
                break
            elif user_age == 18:
                print(f"User's present age is {user_age} and he need to showup for in person review process")
                break
            else:
                print(f"User's present age is {user_age} and his age is falling short by {18 - user_age} Year")
                break
        else:
            continue
except:
    print("Please recheck the code and input provided by you!!!!!!!!!!")
