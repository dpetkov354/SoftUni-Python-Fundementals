def decode():
    data = input()

    while True:
        command = input().split('|')
        current_command = command[0]

        if current_command == 'Decode':
            break

        elif current_command == 'Move':
            n = int(command[1])
            data = data[n:] + data[:n]

        elif current_command == 'Insert':
            index = int(command[1])
            value = command[2]
            data = data[:index] + value + data[index:]

        elif current_command == 'ChangeAll':
            substring = command[1]
            replacement = command[2]
            data = data.replace(substring, replacement)

    print(f"The decrypted message is: {data}")


decode()
