username = input("Your Username : ")
password = input("Your password : ")
if username=="phatcharaphol" and password=="123456789":
    print("Welcome to fish stop monday yummy ")
    print("------------MENU------------")
    print("1.fried rice-------------40-")
    print("2.Omeled-----------------30-")
    print("3.Spagetti---------------70-")

    UserselectedorderA =(input("Enter number of food : "))
    print("-----------your order-----------")
    if UserselectedorderA=="1":
        print("1.fried rice-------------40-")
        price = 40
    elif UserselectedorderA=="2":
        print("2.Omeled-----------------30-")
        price = 30
    elif UserselectedorderA=="3":
        print("3.Spagetti---------------70-")
        price = 70
    amount = int(input("how many : "))

    #total = int(input(UserselectedorderA))+int(input(UserselectedorderB))
    total = price*amount
    print("Total is :",total)
    print("Thank you")
else:
    print("Wrong username or password")
    
