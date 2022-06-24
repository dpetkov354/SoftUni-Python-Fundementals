numbers = list(map(int, input().split(" ")))
average = sum(numbers) / len(numbers)

above_average = [x for x in numbers if x > average]
above_average.sort(reverse=True)

if len(numbers) > 5:
    sorted_list = [x for x in above_average[:5]]
else:
    sorted_list = above_average

array_string = map(str, sorted_list)

if len(above_average) > 0:
    print(" ".join(array_string))
else:
    print("No")
