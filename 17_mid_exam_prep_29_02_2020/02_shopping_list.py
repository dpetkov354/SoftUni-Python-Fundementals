initial_list = list(map(str, input().split("!")))
user_input = input()

while user_input != "Go Shopping!":
    command = []
    command = list(map(str, user_input.split(" ")))
    if command[0] == "Urgent":
        if command[1] not in initial_list:
            initial_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in initial_list:
            initial_list.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in initial_list:
            for item in range(len(initial_list)):
                if initial_list[item] == command[1]:
                    initial_list[item] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in initial_list:
            initial_list.remove(command[1])
            initial_list.append(command[1])
    user_input = input()
print(", ".join(initial_list))
