import read
import write
import operation
import datetime
import random


def option_for_users():
    """This function ask user to sell buy or purchase the laptop with the help of loop"""
    lopp = True
    while lopp == True:
        print("Select your Options to continue")
        print("press 1 to Sell: ")
        print("print 2 for Purchases: ")
        print("Press 3 for Exit: ")
        numberloop = True
        while numberloop:
            try:
                input_from_user = int(input("Enter the option to Continue: "))
            except ValueError as e:
                print("Enter a numeric value")
            else:
                numberloop = False
        print("\n")
        if input_from_user == 1:
            read.display()
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            loop = True
            stringloop = True
            while stringloop:
                user_name = str(input("Enter your Name : "))

                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("The string contains non-alphabetical characters.")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop = False
            stringloop1 = True
            while stringloop1:
                address = str(input("Enter your address: "))

                try:
                    if address.isalpha():
                        break
                    else:
                        raise ValueError("The string contains non-alphabetical characters.")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop1 = False
            numloop = True
            while numloop:
                try:
                    contact_num = int(input("Enter your contact number: "))
                except ValueError:
                    print("Enter a numeric value")
                else:
                    numloop = False

            list = []
            while loop:
                valid_id = True
                dict = read.myfun1()
                while valid_id:
                    laptop_id = operation.validation_lp_num(dict)
                    print(f"Available stocks {dict[laptop_id][3]} only")
                    
                    if dict[laptop_id][3] == 0:
                        operation.loop(valid_id)
                    else:
                        valid_id = False
                quantity_of_laptop = operation.quantity_validation(dict, laptop_id, input_from_user)
                dict = operation.dictonary_update_sell(laptop_id, quantity_of_laptop, list)
                write.update_text(dict)
                loop_1 = True
                while loop_1:
                    ask_again = str(input("Do you want to buy again : "))
                    if ask_again == 'y':
                        loop_1 = False
                        loop = True
                    elif ask_again == 'n':
                        loop_1 = False
                        loop = False
                    else:
                        print("Inappropriate value")
            bill_no = random.randint(0, 500)
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            write.bill_for_sell(user_name, address, contact_num, list, bill_no, date, time)
            write.bill_text_for_sell(user_name, address, contact_num, list, bill_no, date, time)
            print("\n")
            print("Thankyou for you collaboration.")

        elif input_from_user == 2:
            read.display()
            print(
                "------------------------------------------------------------------------------------------------------------------")
            user_name = input("Enter you Name: ")
            dict = read.myfun1()
            list = []
            loop = True
            while loop == True:
                laptop_id = int(input("please!! choose which Id laptop do you want to buy  :  "))
                quantity_of_laptop = operation.quantity_validation(dict, laptop_id, input_from_user)
                dict = operation.dictonary_update_purchase(laptop_id, quantity_of_laptop, list)
                write.update_text(dict)
                loop_1 = True
                while loop_1:
                    ask_again = str(input("Do you want to buy again : "))
                    # print("\n")
                    print("-----------------------------------------------------------------------")
                    if ask_again == 'y':
                        loop_1 = False
                        loop = True
                    elif ask_again == 'n':
                        loop_1 = False
                        loop = False
                    else:
                        print("Inappropriate value")
            bill_no = random.randint(0, 500)
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            write.biil_for_purches(user_name, list, bill_no, date, time)
            write.bill_text_purches(user_name, list, bill_no, date, time)
            print("\n")
            print("Thankyou for you colobration.")
        elif input_from_user == 3:
            loop = False
            print("Thankyou for using our system.")
            print("\n")
        else:
            print("The option you entered", input_from_user, "do not match our system")
            print("\n")
    return input_from_user


option_for_users()
