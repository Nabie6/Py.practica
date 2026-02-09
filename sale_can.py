a =int(input("1 or 2  or 3?: "))
b=float(input("sum: "))

def sale ():
    if a ==1:
        print ("You gold ,with sales: ")
        if b>=100:
            return b-(b*0.2)
        else :
             return b-(b*0.1)
    elif a==2:
       print ("You silver ,with sales: ")
       if b>=100:
            return b-(b*0.15)
       else :
            return b-(b*0.05)
    elif a==3:
       print ("Your total sum: ")
       if b>=100:
            return b-(b*0.05)
       else :
            return b
    else:
        print ("error")

result=sale()
print (f"{result:.2f}")