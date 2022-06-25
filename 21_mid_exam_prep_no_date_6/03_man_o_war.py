pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
health = int(input())
user_input = input()
stalemate = True

while user_input != "Retire":
    command = list(map(str, user_input.split(" ")))
    command_type = str(command[0])

    if command_type == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if len(war_ship) > index >= 0:
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
        else:
            user_input = input()
            continue

    elif command_type == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < end_index and start_index < end_index < len(pirate_ship):
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
        else:
            user_input = input()
            continue

    elif command_type == "Repair":
        index_repair = int(command[1])
        repair = int(command[2])
        if len(pirate_ship) > index_repair >= 0:
            pirate_ship[index_repair] += repair
            if pirate_ship[index_repair] > health:
                pirate_ship[index_repair] = health
        else:
            user_input = input()
            continue

    elif command_type == "Status":
        urgent_sections = 0
        for section in pirate_ship:
            if section < health * 0.2:
                urgent_sections += 1
        print(f"{urgent_sections} sections need repair.")
    for hp in pirate_ship:
        if hp <= 0:
            break
    for hp in war_ship:
        if hp <= 0:
            break
    user_input = input()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}")
