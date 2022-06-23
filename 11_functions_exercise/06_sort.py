def string_to_int(user_input):
    ints = [int(x) for x in user_input]
    print(sorted(ints))


user_input = list(input().split(" "))
string_to_int(user_input)
