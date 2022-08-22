import re


def password_validator():
    password = input()

    while True:
        command = input().split(' ')
        current_command = command[0]

        if current_command == "Complete":
            break

        elif current_command == "Make" and command[1] == "Upper":
            index = int(command[2])
            letter = password[index]
            password = password[:index] + letter.upper() + password[index + 1:]
            print(password)

        elif current_command == "Make" and command[1] == "Lower":
            index = int(command[2])
            letter = password[index]
            password = password[:index] + letter.lower() + password[index + 1:]
            print(password)

        elif current_command == "Insert":
            index = int(command[1])
            char = command[2]

            if 0 <= index <= len(password):
                password = password[:index] + char + password[index:]
                print(password)
            else:
                continue

        elif current_command == "Replace":
            char = command[1]
            char_value = ord(command[1])
            value = int(command[2])
            total_value = char_value + value

            if char in password:
                for i in password:
                    if i == char:
                        original = i
                        replacement = chr(total_value)
                        password = password.replace(original, replacement)
                print(password)
            else:
                continue

        elif current_command == "Validation":
            if len(password) < 8:
                print("Password must be at least 8 characters long!")

            if re.match("^[A-Za-z0-9_]*$", password):
                pass
            else:
                print("Password must consist only of letters, digits and _!")

            upper_char = False
            for ele in password:

                if ele.isupper():
                    upper_char = True
                    break

            if not upper_char:
                print("Password must consist at least one uppercase letter!")

            lower_char = False
            for ele in password:

                if ele.islower():
                    lower_char = True
                    break

            if not lower_char:
                print("Password must consist at least one lowercase letter!")

            is_digit = False
            for ele in password:

                if ele.isdigit():
                    is_digit = True
                    break

            if not is_digit:
                print("Password must consist at least one digit!")


password_validator()
