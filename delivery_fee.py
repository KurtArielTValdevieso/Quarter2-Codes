def fee(x,y):
    yes = round(x * y, 2)
    return yes

dist = float(input("Enter the distance in Kilometers: "))
rate = float(input("Enter rate per kilometer (Philippine pesos): "))

peso_symbol = "\u20B1"

print(f'Total delivery fee: {peso_symbol}{fee(dist,rate)}')