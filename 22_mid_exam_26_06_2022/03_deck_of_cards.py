cards = list(map(str, input().split(", ")))
count_commands = int(input())
if count_commands > 0:
    for loop in range(count_commands):
        command = list(map(str, input().split(", ")))

        if command[0] == "Add":
            if command[1] in cards:
                print("Card is already in the deck")
                continue
            else:
                cards.append(command[1])
                print("Card successfully added")

        elif command[0] == "Remove":
            if command[1] in cards:
                cards.remove(command[1])
                print("Card successfully removed")
            else:
                print("Card not found")
                continue

        elif command[0] == "Remove At":
            index = int(command[1])
            if 0 <= index <= len(cards) - 1:
                cards.pop(index)
                print("Card successfully removed")
            else:
                print("Index out of range")
                continue

        elif command[0] == "Insert":
            index = int(command[1])
            card_name = str(command[2])
            if 0 <= index <= len(cards) - 1 and card_name not in cards:
                cards.insert(index, card_name)
                print("Card successfully added")
            else:
                if 0 <= index <= len(cards) - 1 and card_name in cards:
                    print("Card is already added")
                    continue
                else:
                    print("Index out of range")
                    continue
    print(f"{', '.join((map(str, cards)))}")

else:
    print(f"{', '.join((map(str, cards)))}")
