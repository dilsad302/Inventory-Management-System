def my_header():
    '''this function are used to shows the header part of bill'''
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t \t \t \t  Tanchhopa Laptop Store")
    print("\n")
    print("\t \t \t \t \t \t \t \t  Sallahghari , Bhaktapur  | 9823015455")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("\n")


def myfun1():
    """This function to show the values present in the dictonary"""
    dictonary = {}
    file = open("laptops.txt", "r")
    id_of_laptop = 1
    for data in file:
        data = data.replace("\n", "")
        dictonary.update({id_of_laptop : data.split(",")})
        id_of_laptop += 1
    file.close()
    #print(dictonary)
    return dictonary
 
def display():
    a=1
    """This function  shows laptops details in a table."""
    text= open("laptops.txt","r")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("SN"'\t\t',"Name"'\t\t\t',"Brand"'\t\t\t',"price"'\t\t',"Quantity Aviable",'\t'"Processor"'\t\t',"Graphic Card")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    for value in text:
        print(a, "\t\t"+value.replace(",","\t\t"))
        a= a+1
    return value