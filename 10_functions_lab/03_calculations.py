def type_grade(num_1, num_2, operation):

    if operation == "multiply":
        return num_1 * num_2
    elif operation == "divide":
        return int(num_1 / num_2)
    elif operation == "add":
        return num_1 + num_2
    elif operation == "subtract":
        return num_1 - num_2


operation = input()
num_1 = int(input())
num_2 = int(input())
print(type_grade(num_1, num_2, operation))
