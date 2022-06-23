input_list_string = input()
step = int(input())
number_list = []
list_numbers = input_list_string.split(" ")

for number in list_numbers:
    number_list.append(int(number))

for number in range(step):
    number_list.remove(min(number_list))

print(*number_list, sep=", ")
