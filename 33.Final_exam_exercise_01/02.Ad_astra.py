import re
import math


def ad_astra():
    data = input()
    pattern = r'(\||\#)([A-Z][a-z]+\s[A-Z][a-z]+|[A-Z][a-z]+)(\1)(\d\d/\d\d/\d\d)(\1)(\d+)(\1)'
    result = re.finditer(pattern, data)
    results = []
    calories = 0
    needed_calories_daily = 2000

    for item in result:
        info = item.group()
        results.append(info)

    for i in results:
        if i[0] == "|":
            current_food_data = i.split('|')
            calories += int(current_food_data[3])
        elif i[0] == "#":
            current_food_data = i.split('#')
            calories += int(current_food_data[3])

    days = math.floor(calories / needed_calories_daily)

    print(f"You have food to last you for: {days} days!")
    for n in results:
        if n[0] == "|":
            current_food_data = n.split('|')
            name = current_food_data[1]
            expiration_date = current_food_data[2]
            nutrition = current_food_data[3]
            print(f"Item: {name}, Best before: {expiration_date}, Nutrition: {nutrition}")

        elif n[0] == "#":
            current_food_data = n.split('#')
            name = current_food_data[1]
            expiration_date = current_food_data[2]
            nutrition = current_food_data[3]
            print(f"Item: {name}, Best before: {expiration_date}, Nutrition: {nutrition}")


ad_astra()
