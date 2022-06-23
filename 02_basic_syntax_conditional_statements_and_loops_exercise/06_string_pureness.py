loops = int(input())

for i in range(loops):
    user_input = input()
    pure = True
    for j in range(0, len(user_input)):
        if user_input[j] == "," or user_input[j] == "." or user_input[j] == "_":
            pure = False
    if not pure:
        print(f"{user_input} is not pure!")
    else:
        print(f"{user_input} is pure.")