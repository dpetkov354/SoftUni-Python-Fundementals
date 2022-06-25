journal = list(map(str, input().split(", ")))
user_input = input()

while user_input != "Craft!":
    command = list(map(str, user_input.split(" - ")))

    if command[0] == "Collect":
        item = command[1]
        if item in journal:
            user_input = input()
            continue
        else:
            journal.append(item)

    elif command[0] == "Drop":
        item = command[1]
        if item in journal:
            journal.remove(item)
        else:
            user_input = input()
            continue

    elif command[0] == "Combine Items":
        items_for_combo = list(map(str, command[1].split(":")))
        old_item = items_for_combo[0]
        new_item = items_for_combo[1]

        if old_item in journal:
            old_item_index = journal.index(old_item) + 1
            journal.insert(old_item_index, new_item)
        else:
            user_input = input()
            continue

    elif command[0] == "Renew":
        item = command[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)
        else:
            user_input = input()
            continue

    user_input = input()

print(f"{', '.join((map(str, journal)))}")
