loops = int(input())
total_capacity = 255
current_liters = 0

for i in range(loops):
    liters = int(input())
    current_liters += liters
    if current_liters > total_capacity:
        current_liters -= liters
        print("Insufficient capacity!")
print(current_liters)
