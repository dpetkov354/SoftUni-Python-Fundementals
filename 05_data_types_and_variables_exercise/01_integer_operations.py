import math

add_a = int(input())
add_b = int(input())
divide = int(input())
multiply = int(input())

result = math.floor(math.floor((add_a + add_b) / divide)) * multiply
print(round(result))
