def Vatcalculator(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
totalprice =int(input("tatalprice : "))
Vatcalculator(totalprice)
print("Total is : %f "%(Vatcalculator(totalprice)))
