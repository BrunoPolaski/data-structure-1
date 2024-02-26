vehiclePrice = input("Enter the price of the vehicle: ")
installments = input("Enter the number of installments: ")
tax = input("Enter the tax: ")
def calcTotalValue(vehiclePrice, installments, tax):
    return vehiclePrice * (1 + (installments * tax))

print("The total value is", calcTotalValue(vehiclePrice, installments, tax))