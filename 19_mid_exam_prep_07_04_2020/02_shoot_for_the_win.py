initial_list = list(map(int, input().split(" ")))
user_input = input()
shoot_count = 0

while user_input != "End":
    shoot = int(user_input)
    if shoot > len(initial_list) - 1:
        user_input = input()
        continue
    shoot_count += 1
    current_shot_value = initial_list[shoot]
    initial_list[shoot] = -1
    for i in range(0, len(initial_list)):
        if initial_list[i] > current_shot_value and initial_list[i] != -1:
            initial_list[i] -= current_shot_value
        elif initial_list[i] <= current_shot_value and initial_list[i] != -1:
            initial_list[i] += current_shot_value
    user_input = input()

print(f"Shot targets: {shoot_count} -> {' '.join((map(str, initial_list)))}")
