                                    #*******************************************************#
                                    #**********************   MyCart  **********************#
                                    #*******************************************************#
from datetime import datetime
from Utils import product

print("\t"*6,"*"*33,"\n","\t"*6,"|","\t","WelCome To MyCart","\t","|","\n","\t"*6,"*"*33)
while True:
    user_cart = []
    total_amount = 0
    cnt = 0
    auth = '123456'
    pro_details = []
    try:
        while True:
            print("\n\t","Type of Visitor","\n\t", "Enter '1' if you are 'USER'","\n\t" , "Enter '2' if you are 'ADMIN'")
            get_input = input("\n\t Enter Your Choice > ")
            if get_input == "1":
                user_status = 1
                break
            elif get_input == '2':
                break
            else:
                continue
    except Exception as e:
        print(e)


    if get_input == '1':
        get_user_name = input("\n\t Please enter your name: ")
        print("\n\t",">> Hello", get_user_name,"<<")
        try:
            while True:
                category = list(product.cat_list.keys())
                print("\n\t","Following are the available product Category","\n\t",category)
                user_choice = input("\n\t Enter Your Choice > ")
                brands = list(product.cat_list.get(user_choice))
                print("\n\t","Following are the available Brand's","\n\t",brands)
                user_choice = input("\n\t Enter Your Choice > ")
                models = list(product.product_list.get(user_choice))
                print("\n\t","Following are the available Models's","\n\t",models)
                user_choice = input("\n\t Enter Your Choice > ")
                item = list(product.model_details.get(user_choice))
                print("\n\t","Product Details of",user_choice,"\n\t",item)
                cart_status = input("\n\t Enter 1 -> Add To Cart \n\t Enter 2 -> Shop More \n\t Enter 3 -> Checkout \n\t Enter 4 -> RemoveItem \n\t Enter Your Choice > ")
                if cart_status == '1':
                    cnt += 1
                    user_cart.append({user_choice:list(item[-1].values())})
                    pro_details.append(item)
                    print("\n\t","Product", user_choice, "is added to cart")
                    continue
                elif cart_status == '2':
                    continue
                elif cart_status == '3':
                    get_current_pro = input("\n\t Enter '1' -> To Checkout with current Product \t Enter '2' -> To Checkout without current Product >")
                    if get_current_pro == '1':
                        cnt += 1
                        user_cart.append({user_choice:list(item[-1].values())})
                        pro_details.append({user_choice:item})
                        print("\n\t","Product", user_choice, "is added to cart")
                        break
                    elif get_current_pro =='2':
                        break
                    else:
                        pass
                elif cart_status == '4':
                    get_item = input("\n\t Enter item Name to Remove it from Cart > ")
                    for temp in range(len(user_cart)):
                        if get_item in list(user_cart[temp].keys()):
                            print("IN")
                            user_cart.pop(temp)
                            pro_details.pop(temp)
                            break
                        else:
                            print("\n\t Item not in Cart")
            for temp in user_cart:
                a = float(str(list(temp.values())).replace("[","").replace("]","").replace("'","").replace('"','').replace(",",""))
                total_amount += a
            if total_amount > 10000:
                print("\n\t","Your Total Payable Amount is :",total_amount, "for" ,len(user_cart),"Products",
                "\n\t","As your grand total is more then 10,000.00 you are getting discount of 500,", 
                "Hence final Payable Amount is : ",total_amount - 500)
            else:
                print("\n\t","Your Total Payable Amount is :",total_amount, "for" ,len(user_cart),"Products")
            
            print("\n","*"*120)
            output = str(datetime.now()) + "," + get_user_name + "," + str(user_cart)+ ","+ str(pro_details) + "," + str(total_amount) + "\n"
            with open("billing_records.csv", "a") as f:
                f.write(output)
        except Exception as e:
            print(e)

    elif get_input == '2':
        get_auth_code = input("\n\t Enter Security Code to get Admin Access > ")
        if get_auth_code == auth:
            admin_choice = input("\n\t Enter 1 -> Add To Categories \n\t Enter 2 -> View Bills. \n\t Enter Your Choice > ")
            if admin_choice == '1':
                Category_name = input("\n\t Enter Category name > ")
                Brand_name = input("\n\t Enter Brands name > ")
                product.cat_list[Category_name] = list([Brand_name])
                print("\n\t",product.cat_list)
                Model_name = input("\n\t Enter Model names > ")
                product.product_list[Brand_name] = list([Model_name])
                print("\n\t",product.product_list)
                add_info = input("\n\t Enter 'Y/y' -> Add To Info -> Add and 'N/0' -> Exit > ")
                info_list = []
                while add_info in 'Yy':
                    key = input('\n\t Enter Key > ')
                    value = input('\n\t Value Key > ')
                    info_list.append({key:value})
                    add_info = input("\n\t Enter 'Y/y' -> Add Add To and 'N/n' -> Exit > ")
                    if add_info in 'Yy':
                        continue
                    else:
                        break
                product.model_details[Model_name] = info_list
                print("\n\t",product.model_details)
            elif admin_choice == '2':
                with open("billing_records.csv") as f:
                    bill = f.read()
                print('\n\t',bill)
    else:
        pass
    print("\n","*"*120)
    