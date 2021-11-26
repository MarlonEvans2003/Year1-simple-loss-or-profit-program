def CostPrice():
    while True:
        Cost = input("Please enter how much the item costs: ")
        while Cost.isdigit() == True:
            if int(Cost) > 0:
                return (Cost)
                break
        else:
            print("Please enter a positive number")

def SellPrice():
    while True:
        Sell = input("Please enter how much you sold the item for: ")
        if Sell.isdigit() == True:
            if int(Sell) > 0:
                return (Sell)
                break
        else:
            print("Please enter a positive number")

def calculation():
    if Cost > Sell:
        FinalPrice = Sell - Cost
        print ("Your total Loss is: " + str(FinalPrice))
    else:
        FinalPrice = Sell - Cost
        print("Your total profit is: " + str(FinalPrice))



############
#
# Main
#
###########
while True:
    Cost = CostPrice()
    Cost = float(Cost)
    Sell = SellPrice()
    Sell = float(Sell)
    calculation()
    Return = int(input("Do you want to enter another item? 1. Yes 2.No: "))
    if Return == 1:
        print("Okay!")
    elif Return == 2:
        print("GoodBye!")
        break
    else:
        print("Please enter a valid choice:")
        
