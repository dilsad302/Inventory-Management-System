import read
def update_text(dict):
    open_file=open("laptops.txt","w")
    for i in dict.values():
        open_file.write(str(i[0])+","+ str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
        open_file.write("\n")
    open_file.close()

def bill_for_sell(name,address,contact_num,list,bill_no,date,time):
    global ship
    ship = input("Do you want to ship")
    ship_1= True
    while ship_1:
        if ship.lower() == "y":
            ship_1=False
            ship_cost=250
        elif ship.lower() == "n":
            ship_1 = False
        else:
            print("Unappropriate value")
    read.my_header()
    print(f"\t\t\t\t\tBill no: {bill_no}")
    print(f"date: {date}\t\t\t\t\t Time: {time}")
    print(f"name:  {name}")
    print(f"Address: {address}")
    print(f"Number: {contact_num}")
    t_total=0


    for i in range(len(list)):
        c_name=list[i][1].replace(" ","")
        print(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}") 
        price1 =list[i][2].replace(" ","")
        print(f"Price: {price1}\t\t\t Quantity: {list[i][4]}")
        print(f"Total price: {list[i][3]}")
        t_total=t_total+int(list[i][3])
        print(f"\n")
    if ship=="y":
        print(f"Shipping cost: {250}")
        print(f"Total: {t_total}")
        print(f"Grand total: {t_total+250}")
    else:
        print(f"Total: {t_total}")


def bill_text_for_sell(name,address,contact_num,list,bill_no,date,time):
    file = open(f"{bill_no}.txt","w")
    file.write(f"/t/t/tBill no: {bill_no}\n")
    file.write(f"date: {date}\t\t\t\t\t Time: {time}\n")
    file.write(f"name:  {name}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Number: {contact_num}\n")
    t_total=0

    for i in range(len(list)):
        c_name=list[i][1].replace(" ","")
        file.write(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}\n")
        price1 =list[i][2].replace(" ","")
        file.write(f"Price: {price1}\t\t\t\t\t Quantity: {list[i][4]}\n")
        file.write(f"Total price: {list[i][3]}\n")
        t_total=t_total+int(list[i][3])
        file.write(f"\n")
    if ship=="y":
        file.write(f"Shipping cost: {250}\n")
        file.write(f"Total: {t_total}\n")
        file.write(f"Grand total: {t_total+250}\n")
    else:
        file.write(f"Total: {t_total}\n")

def biil_for_purches(name,list,bill_no,date,time):

    print(f"\t\t\t\t\tBill no: {bill_no}")
    print(f"date: {date}\t\t\t\t\t Time: {time}")
    print("-------------------------------------------------------------------------")
    print(f"name:  {name}")
    t_total=0


    for i in range(len(list)):
        c_name=list[i][1].replace(" ","")
        print(f"Laptop Name: {list[i][0]}\t\tCompany Name: {c_name}") 
        price1 =list[i][2].replace(" ","")
        print(f"Price: {price1}\t\t \nQuantity: {list[i][4]}")
        print(f"Total price: {list[i][3]}")
        t_total=t_total+int(list[i][3])
        print(f"\n")
    print(f"vat amount: {0.13*t_total}")
    print(f"Grand Total :{(0.13*t_total) + t_total}")

def bill_text_purches(name,list,bill_no,date,time):
    file = open(f"{bill_no}.txt","w")
    file.write(f"\\t\t\t\tBill no: {bill_no}\n")
    file.write(f"date: {date}\t\t\t\t\t Time: {time}\n")
    file.write(f"name:  {name}\n")
    t_total=0

    for i in range(len(list)):
        c_name=list[i][1].replace(" ","")
        file.write(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}\n")
        price1 =list[i][2].replace(" ","")
        file.write(f"Price: {price1}\t\t\t\t\t \nQuantity: {list[i][4]}\n")
        file.write(f"Total price: {list[i][3]}\n")
        t_total=t_total+int(list[i][3])
        file.write(f"\n")
    file.write(f"vat amount: {0.13*t_total}\n")
    file.write(f"Grand Total = {(0.13*t_total) + t_total}\n")