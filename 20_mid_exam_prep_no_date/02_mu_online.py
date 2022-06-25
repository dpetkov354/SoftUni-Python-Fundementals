rooms = list(map(str, input().split("|")))
starting_hp = 100
starting_bitcoins = 0

for room in range(0, len(rooms)):
    current_room = list(map(str, rooms[room].split(" ")))
    type_of_room = str(current_room[0])
    amount_room = int(current_room[1])

    if type_of_room == "potion":
        starting_hp += amount_room
        if starting_hp > 100:
            over_healing = (starting_hp - 100)
            actual_healing = amount_room - over_healing
            starting_hp = 100
        else:
            actual_healing = amount_room
        print(f"You healed for {actual_healing} hp.")
        print(f"Current health: {starting_hp} hp.")

    elif type_of_room == "chest":
        starting_bitcoins += amount_room
        print(f"You found {amount_room} bitcoins.")

    else:
        monster = type_of_room
        damage = amount_room
        starting_hp -= damage
        if starting_hp > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room + 1}")
            break
if starting_hp > 0:
    print(f"You've made it!\nBitcoins: {starting_bitcoins}\nHealth: {starting_hp}")
