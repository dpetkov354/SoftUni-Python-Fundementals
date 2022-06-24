targets = list(map(int, input().split(" ")))
user_input = input()

while user_input != "End":
    shoot = list(map(str, user_input.split(" ")))
    if shoot[0] == "Shoot":
        index_value = int(shoot[1])
        power_value = int(shoot[2])
        if 0 <= index_value <= len(targets) - 1:
            targets[index_value] -= power_value
            if targets[index_value] <= 0:
                targets.pop(index_value)
    if shoot[0] == "Add":
        index_value = int(shoot[1])
        power_value = int(shoot[2])
        if 0 <= index_value <= len(targets) - 1:
            targets.insert(index_value, power_value)
        else:
            print("Invalid placement!")
    if shoot[0] == "Strike":
        index_value = int(shoot[1])
        power_value = int(shoot[2])
        if 0 + power_value <= index_value <= len(targets) - 1 - power_value:
            for p in range(1, power_value + 1):
                targets.pop(index_value + p)
                targets.pop(index_value - p)
            targets.pop(index_value - power_value)
        else:
            print("Strike missed!")
    user_input = input()

print(f"{'|'.join((map(str, targets)))}")
