list_of_numbers = input().split()
opposite_numbers = []
for current_index in range(len(list_of_numbers)):
    current_number = int(list_of_numbers[current_index])
    opposite_numbers.append(-current_number)
print(opposite_numbers)
