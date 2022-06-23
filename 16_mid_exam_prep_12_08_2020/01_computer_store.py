total_price = 0
taxed_price = 0
special_discount = 0

loop = True
while loop:
    command = input()
    if command == "special" or command == "regular":
        loop = False
        continue
    price = float(command)
    if price <= 0:
        print("Invalid price!")
        continue
    total_price += price

if total_price == 0:
    print("Invalid order!")
elif command == "special":
    taxed_price = (total_price * 1.2) - total_price
    special_discount = 0.9
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:0.2f}$\nTaxes:"
          f" {taxed_price:0.2f}$\n-----------\nTotal price: {(taxed_price + total_price) * special_discount:0.2f}$")
elif command == "regular":
    taxed_price = (total_price * 1.2) - total_price
    special_discount = 1
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:0.2f}$\nTaxes:"
          f" {taxed_price:0.2f}$\n-----------\nTotal price: {(taxed_price + total_price) * special_discount:0.2f}$")
