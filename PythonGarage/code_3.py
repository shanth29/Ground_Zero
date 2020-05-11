""" 
Faulty Calculator : Write a code to get two values along with arithmetic operator that he wants to perform. 
This calculator should provide correct result except for these three calculations(45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4)
"""
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def multi(a,b):
    return a*b


operator = {"+":"add", "-":"sub", "/":"div", "*":"multi"}
start = 0
try:
    while True: 
        input_value1 = input("Enter the Num1:")
        input_value2 = input("Enter the Num2:")
        input_value3 = input("Enter the Operator:")
        if "" not in {input_value1,input_value2,input_value3}:
            if input_value1.isnumeric() and input_value2.isnumeric() and input_value3 in operator:
                temp = input_value1 +" "+ input_value3 +" "+ input_value2
                if temp == "43 * 3":
                    print(f"Result of {input_value1} {input_value3} {input_value2} = 555")
                    break
                elif temp == "56 + 9":
                    print(f"Result of {input_value1} {input_value3} {input_value2} = 77")
                    break
                elif temp == "56 / 6":
                    print(f"Result of {input_value1} {input_value3} {input_value2} = 4")
                    break
                else:
                    for y,z in operator.items():
                        if y == input_value3:
                            if z == "add":
                                result = add(int(input_value1),int(input_value2))
                                print(f"Your have entered {input_value1}{input_value3}{input_value2} and output is {result}")
                                break
                            elif z == "sub":
                                result = sub(int(input_value1),int(input_value2))
                                print(f"Your have entered {input_value1}{input_value3}{input_value2} and output is {result}")
                                break
                            elif z == "div":
                                result = div(int(input_value1),int(input_value2))
                                print(f"Your have entered {input_value1}{input_value3}{input_value2} and output is {result}")
                                break
                            elif z == "multi":
                                result = multi(int(input_value1),int(input_value2))
                                print(f"Your have entered {input_value1}{input_value3}{input_value2} and output is {result}")
                                break
                            else:
                                pass
                        else:
                            pass
                    break
            else:
                print("Please Enter correct Input")
        else:
            print("Please Enter Input")

except Exception as e:
    print(e)


