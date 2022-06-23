def string_to_int(user_input):
    ints = [int(x) for x in user_input]
    return ints


def odd_sum(numbers):
    sum_odd = 0
    for n in numbers:
        if n % 2 != 0:
            sum_odd += n
    return sum_odd


def even_sum(numbers):
    sum_even = 0
    for n in numbers:
        if n % 2 == 0:
            sum_even += n
    return sum_even


user_input = list(input())
print(f'Odd sum = {odd_sum(string_to_int(user_input))}, Even sum = {even_sum(string_to_int(user_input))}')
