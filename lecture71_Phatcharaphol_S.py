menuList = []
priceList = []
while True :
    menuName = input("Please Enter menu : ")
    if(menuName.lower()== "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
print("---------Your Order---------")
for i in range(len(menuList)):
    print(menuList[i],priceList[i])
print("Total : ",sum(priceList))
print("----------------------------")
