def minn(user_input):
    ints = [int(x) for x in user_input]
    print(f'The minimum number is {min(ints)}')


def maxx(user_input):
    ints = [int(x) for x in user_input]
    print(f'The maximum number is {max(ints)}')


def summ(user_input):
    ints = [int(x) for x in user_input]
    print(f'The sum number is: {sum(ints)}')


user_input = list(input().split(" "))
minn(user_input)
maxx(user_input)
summ(user_input)
