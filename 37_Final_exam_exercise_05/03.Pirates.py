def create_cities(cities):
    while True:
        city = input()

        if city == "Sail":
            break

        city_info = city.split('||')
        city_name = city_info[0]
        city_population = int(city_info[1])
        city_gold = int(city_info[2])
        if city_name not in cities:
            cities[city_name] = [city_population, city_gold]
        else:
            cities[city_name][0] += city_population
            cities[city_name][1] += city_gold


def pillage_cities(cities):
    while True:
        command = input().split('=>')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'Plunder':
            town = command[1]
            people = int(command[2])
            gold = int(command[3])
            cities[town][0] -= people
            cities[town][1] -= gold

            if cities[town][0] <= 0 or cities[town][1] <= 0:
                del cities[town]
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
                print(f"{town} has been wiped off the map!")
            else:
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        elif current_command == 'Prosper':
            town = command[1]
            gold = int(command[2])

            if gold < 0:
                print(f"Gold added cannot be a negative number!")
                continue
            else:
                cities[town][1] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    if len(cities) == 0:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for town in cities:
            print(f"{town} -> Population: {cities[town][0]} citizens, Gold: {cities[town][1]} kg")

    return cities


def pirates():
    cities = {}

    create_cities(cities)
    pillage_cities(cities)


pirates()
