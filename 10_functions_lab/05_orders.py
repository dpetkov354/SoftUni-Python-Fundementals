def order(str, q):
    if str == "coffee":
        price = 1.50
    elif str == "coke":
        price = 1.40
    elif str == "water":
        price = 1.00
    elif str == "snacks":
        price = 2.00
    return f'{price * q:.2f}'


type = input()
quantity = int(input())

print(order(type, quantity))
