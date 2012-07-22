# Global Constants! 
BURGER_PRICE = float(0.99)
FRY_PRICE = float(0.79)
SODA_PRICE = float(1.09)
TAX_RATE = float(0.06)

# The main function.
def main():
    done = str("no")
    orderInput = int(0)
    numberBurgers = int(0)
    numberFries = int(0)
    numberSodas = int(0)
    while done != "yes" and done != "y" and done != "Y" and done != "Yes" and done != "YES":
        print("For Yum Yum Burger, please enter 1.")
        print("For Grease Yum Fries, please enter 2.")
        print("For Soda Yum, please enter 3.")
        orderInput = input("Please enter your selection: ")
        if orderInput == 1:
            numberBurgers = int(getNumber(orderInput))
            done = raw_input("Will that complete your order? (Y/N) ")
        elif orderInput == 2:
            numberFries = int(getNumber(orderInput))
            done = raw_input("Will that complete your order? (Y/N) ")
        elif orderInput == 3:
            numberSodas = int(getNumber(orderInput))
            done = raw_input("Will that complete your order? (Y/N) ")
        else:
            print("Error! You didn\'t put in 1, 2, or 3 as your selection! Please try again!")
            done = raw_input("Will that complete your order? (Y/N) ")
    totalBurgers = float(numberBurgers * BURGER_PRICE)
    totalFries = float(numberFries * FRY_PRICE)
    totalSodas = float(numberSodas * SODA_PRICE)
    subTotal = float(totalBurgers + totalFries + totalSodas)
    taxTotal = float(TAX_RATE * subTotal)
    completeTotal = float(taxTotal + subTotal)
    dispReceipt(numberBurgers, totalBurgers, numberFries, totalFries, numberSodas, totalSodas, subTotal, taxTotal, completeTotal)

# Function to get the number of each item ordered.
def getNumber(orderInput):
    returnNumber = int(0)
    if orderInput == 1:
        returnNumber = int(input("How many Yum Yum Burgers would you like? "))
    if orderInput == 2:
        returnNumber = int(input("How many orders of Grease Yum Fries would you like? "))
    if orderInput == 3:
        returnNumber = int(input("How many cups of Soda Yum would you like? "))
    return returnNumber

# Output!
def dispReceipt(numberBurgers, totalBurgers, numberFries, totalFries, numberSodas, totalSodas, subTotal, taxTotal, completeTotal):
    print("Yum Yum Burgers: ", numberBurgers, " @ $", BURGER_PRICE, ": $", totalBurgers)
    print("Grease Yum Fries:", numberFries, " @ $", FRY_PRICE, ": $", totalFries)
    print("Soda Yum:", numberSodas, " @ $", SODA_PRICE, ": $", totalSodas)
    print("Sub-Total:$", subTotal)
    print("Tax@ ", TAX_RATE, "%: $", taxTotal)
    print("Total:$", completeTotal)

# Start
main()

# End
