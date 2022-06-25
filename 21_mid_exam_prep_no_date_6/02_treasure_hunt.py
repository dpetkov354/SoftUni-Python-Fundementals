loot = list(map(str, input().split("|")))
user_input = input()
stolen_item_list = []
size_of_treasure = 0

while user_input != "Yohoho!":
    command = list(map(str, user_input.split(" ")))
    command_type = str(command[0])

    if command_type == "Loot":
        for looted_item in range(1, len(command)):
            if command[looted_item] in loot:
                continue
            else:
                loot.insert(0, command[looted_item])

    elif command_type == "Drop":
        position = int(command[1])
        if len(loot) - 1 >= position >= 0:
            dropped_item = loot[position]
            loot.remove(dropped_item)
            loot.append(dropped_item)
        elif len(loot) * -1 <= position < 0:
            dropped_item = loot[position]
            loot.remove(dropped_item)
            loot.append(dropped_item)
        else:
            user_input = input()
            continue

    elif command_type == "Steal":
        count = int(command[1])
        stolen_item_list = []
        if count > len(loot):
            count = len(loot)
        for stolen_items in range(0, count):
            current_item_for_stealing = loot[-1]
            stolen_item_list.append(current_item_for_stealing)
            loot.remove(current_item_for_stealing)
        stolen_item_list.reverse()
        print(f"{', '.join((map(str, stolen_item_list)))}")
    user_input = input()

if len(loot) > 0:
    for item in loot:
        length = len(item)
        size_of_treasure += length

    average = size_of_treasure / len(loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
