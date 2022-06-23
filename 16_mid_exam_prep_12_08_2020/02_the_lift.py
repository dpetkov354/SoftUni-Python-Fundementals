people_in_line = int(input())
starting_people_in_line = people_in_line
wagons = list(map(int, input().split(" ")))
free_seats = (len(wagons) * 4) - sum(wagons)

for index, num_of_wagon in enumerate(wagons):
    if num_of_wagon > 3:
        continue
    else:
        diff = 4 - num_of_wagon
        if people_in_line < diff:
            wagons[index] += people_in_line
            people_in_line = 0
        else:
            people_in_line -= diff
            wagons[index] += diff

if free_seats > starting_people_in_line:
    print(f"The lift has empty spots!\n{' '.join(map(str, wagons))}")
elif free_seats == starting_people_in_line:
    print(f"{' '.join(map(str, wagons))}")
else:
    print(f"There isn't enough space! {people_in_line} people in a queue!\n{' '.join(map(str, wagons))}")
