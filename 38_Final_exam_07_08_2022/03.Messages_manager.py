def messages_manager(number):
    users_limit = number
    users = {}

    while True:
        command = input().split('=')
        current_command = command[0]

        if current_command == "Statistics":
            break

        elif current_command == "Add":
            name = command[1]
            total = int(command[2]) + int(command[3])

            if name not in users:
                users[name] = total
            else:
                continue

        elif current_command == "Message":
            sender = command[1]
            receiver = command[2]

            if sender in users and receiver in users:
                users[sender] += 1
                users[receiver] += 1

                if users[sender] >= users_limit:
                    print(f"{sender} reached the capacity!")
                    users.pop(sender)

                if users[receiver] >= users_limit:
                    print(f"{receiver} reached the capacity!")
                    users.pop(receiver)

        elif current_command == "Empty":
            current_user = command[1]

            if current_user == "All":
                users.clear()

            elif current_user in users:
                users.pop(current_user)

    print(f"Users count: {len(users)}")
    for key, value in users.items():
        print(f"{key} - {value}")


max_messages = int(input())
messages_manager(max_messages)
