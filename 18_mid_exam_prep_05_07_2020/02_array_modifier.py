array = list(map(int, input().split(" ")))
user_input = input()

while user_input != "end":
    command = list(map(str, user_input.split(" ")))
    if command[0] == "swap":
        index_one = int(command[1])
        index_two = int(command[2])
        place_holder_one = array[index_one]
        place_holder_two = array[index_two]
        array[index_one] = place_holder_two
        array[index_two] = place_holder_one
    elif command[0] == "multiply":
        first = int(command[1])
        second = int(command[2])
        array[first] *= array[second]
    elif command[0] == "decrease":
        for a in range(len(array)):
            array[a] = array[a] - 1
    user_input = input()

array_string = map(str, array)
print(", ".join(array_string))
