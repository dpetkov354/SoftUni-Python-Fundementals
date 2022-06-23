user_input = ""
while user_input != "End":
    user_input = input()
    output = ""
    if user_input != "SoftUni" and user_input != "End":
        for i in range(len(user_input)):
            output = output + user_input[i]
            output = output + user_input[i]
    else:
        continue
    print(output)
