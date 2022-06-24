first_capacity = int(input())
second_capacity = int(input())
third_capacity = int(input())
capacity_per_hour = first_capacity + second_capacity + third_capacity
students_count = int(input())
hour = 0

while students_count > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    else:
        students_count -= capacity_per_hour

print(f"Time needed: {hour}h.")
