def discount(i):
    nettprice = 0.8 * i
    return nettprice

price = float(input("Enter Price: "))
price = discount(price)
print(price)