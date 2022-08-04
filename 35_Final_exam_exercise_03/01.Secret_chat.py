def secret_chat():
    data = input()

    while True:
        user_input = input()

        if user_input == 'Reveal':
            break

        command = user_input.split(':|:')
        current_command = command[0]

        if current_command == 'InsertSpace':
            index = int(command[1])
            data = data[:index] + " " + data[index:]

        elif current_command == 'Reverse':
            sub_string = command[1]
            reversed_string = ''.join(reversed(sub_string))
            if sub_string in data:
                data = data.replace(sub_string, "", 1)
                data = data + reversed_string
            else:
                print("error")
                continue

        elif current_command == 'ChangeAll':
            sub_string = command[1]
            replacement = command[2]
            data = data.replace(sub_string, replacement)
        print(data)
    print(f"You have a new text message: {data}")


secret_chat()
