loops = int(input())
total = 0
for i in range(loops):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if not 0.01 <= capsule_price <= 100.00 or not 1 <= capsule_per_day <= 2000 or not 1 <= days <= 31:
        continue
    price_coffee = (capsule_per_day * capsule_price) * days
    total += price_coffee
    print(f"The price for the coffee is: ${price_coffee:.2f}")
print(f"Total: ${total:.2f}")
