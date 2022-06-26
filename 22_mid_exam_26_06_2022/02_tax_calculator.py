import math
car_list = list(map(str, input().split(">>")))
total_tax = 0

for car in range(len(car_list)):
    current_car = list(map(str, car_list[car].split(" ")))
    car_type = current_car[0]
    tax_years = int(current_car[1])
    car_km = int(current_car[2])

    if car_type == "family":
        initial_tax = 50
        decline_per_year = 5
        increase_per_3000_km = 12
        passed_km = car_km // 3000
        car_tax = passed_km * increase_per_3000_km + (initial_tax - tax_years * decline_per_year)
        total_tax += car_tax
        print(f"A {car_type} car will pay {car_tax:.2f} euros in taxes.")

    elif car_type == "heavyDuty":
        initial_tax = 80
        decline_per_year = 8
        increase_per_9000_km = 14
        passed_km = car_km // 9000
        car_tax = passed_km * increase_per_9000_km + (initial_tax - tax_years * decline_per_year)
        total_tax += car_tax
        print(f"A {car_type} car will pay {car_tax:.2f} euros in taxes.")

    elif car_type == "sports":
        initial_tax = 100
        decline_per_year = 9
        increase_per_2000_km = 18
        passed_km = car_km // 2000
        car_tax = passed_km * increase_per_2000_km + (initial_tax - tax_years * decline_per_year)
        total_tax += car_tax
        print(f"A {car_type} car will pay {car_tax:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")