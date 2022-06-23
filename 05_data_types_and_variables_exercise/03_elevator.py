import math

people = int(input())
capacity = int(input())
full_trips = math.floor(people / capacity)
if people % capacity != 0:
    full_trips += 1
print(full_trips)
