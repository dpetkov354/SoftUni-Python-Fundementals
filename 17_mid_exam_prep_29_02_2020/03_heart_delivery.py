initial_list = list(map(int, input().split("@")))
user_input = input()
current_position_index = 0
failed_count = 0
list_length = len(initial_list)

while user_input != "Love!":
    command = []
    command = list(map(str, user_input.split(" ")))
    jump_range = int(command[1])
    if command[0] == "Jump" and 1 <= jump_range <= 20:
        if jump_range > list_length - (current_position_index + 1):
            current_position_index = 0
        elif jump_range == list_length:
            jump_range = 0
        else:
            current_position_index += jump_range
        if initial_list[current_position_index] == 0:
            print(f"Place {current_position_index} already had Valentine's day.")
        elif initial_list[current_position_index] == 2:
            initial_list[current_position_index] -= 2
            print(f"Place {current_position_index} has Valentine's day.")
        else:
            initial_list[current_position_index] -= 2
        user_input = input()
if user_input == "Love!":
    print(f"Cupid's last position was {current_position_index}.")
    if sum(initial_list) == 0:
        print("Mission was successful.")
    else:
        for house in initial_list:
            if house != 0:
                failed_count += 1
        print(f"Cupid has failed {failed_count} places.")
