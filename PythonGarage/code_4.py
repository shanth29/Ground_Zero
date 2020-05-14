""" 
Number Guessing Challenge : Hide a pre defined number and ask user to guess the Number and tell him how close his guess was with 
every guess and limit the number of guess and print the same and finally print Game Over if user finish his limit count without correct guess.
"""

# hidden_num = int(input("Enter the Number you want to hide:"))
hidden_num = 56
_count = 0
print("""\t\t\tTips to Play Game!!!!!!!!!!!!!!!!!
        1. If the difference between Guessed no. and Hidden no. is more then 30 --> 'Your are "Too Far" from Number'
        2. If the difference between Guessed no. and Hidden no. is less then 05 --> 'Your are "Too Close" from Number'
        3. If the difference between Guessed no. and Hidden no. is less then 30 but more then 10 --> 'Your are "Far" from Number',
        4. If the difference between Guessed no. and Hidden no. is more then 05 but less then 10--> 'Your are "Close" from Number'
        """)
try:
    while _count < 5:
        print("You have limit of << 5 >> to guess the number and your remaining guessing limit is", 5-_count)
        num_guessed = input("Guess the Number:")
        if num_guessed.isnumeric() and num_guessed != "":
            _count += 1
            num_guessed = int(num_guessed)
            if hidden_num == num_guessed:
                print(f"Bingo you have taken {_count} attempt to guess Correct Number")
                break
            elif hidden_num > num_guessed:
                result = hidden_num - num_guessed
                if result >= 30:
                    print("Your are 'Too Far' from Number")
                elif result < 30 and result >=10:
                    print("Your are 'Far' from Number")
                elif result < 10 and result >= 5:
                    print("Your are 'Close' from Number")
                elif result < 5:
                    print("Your are 'Too Close' from Number")
            else:
                result = num_guessed - hidden_num
                if result >= 30:
                    print("Your are 'Too Far' from Number")
                elif result < 30 and result >=10:
                    print("Your are 'Far' from Number")
                elif result < 10 and result >= 5:
                    print("Your are 'Close' from Number")
                elif result < 5:
                    print("Your are 'Too Close' from Number")
        else:
            continue
    else:
        print("GAME OVER!!!!!! You have attempted maximum number of Guess.")

except Exception as e:
    print(e)