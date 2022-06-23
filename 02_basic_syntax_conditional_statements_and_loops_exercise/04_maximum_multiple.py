divisor = int(input())
boundary = int(input())
largest_n = 1

for i in range(1, boundary + 1):

    if i % divisor == 0:
        if i > largest_n:
            largest_n = i
print(largest_n)
