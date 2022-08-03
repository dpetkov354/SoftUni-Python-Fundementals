def world_tour():
    data = input()

    while True:
        user_input = input()

        if user_input == 'Travel':
            break

        command = user_input.split(':')
        current_command = command[0]

        if current_command == 'Add Stop':
            index = int(command[1])
            string = str(command[2])
            if len(data) > index >= 0:
                data = data[:index] + string + data[index:]

        elif current_command == 'Remove Stop':
            start_index = int(command[1])
            end_index = int(command[2])
            if len(data) > start_index >= 0 and len(data) > end_index >= 0:
                data = data[:start_index] + "" + data[end_index+1:]

        elif current_command == 'Switch':
            old_string = str(command[1])
            new_string = str(command[2])
            if old_string in data:
                data = data.replace(old_string, new_string)
        print(data)
    print(f"Ready for world tour! Planned stops: {data}")


world_tour()
