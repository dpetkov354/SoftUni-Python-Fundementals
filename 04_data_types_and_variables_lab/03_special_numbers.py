loop = int(input())

for i in range(1, loop + 1):
    sum_digits = 0
    digit = i
    for j in str(digit):
        sum_digits += int(j)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{digit} -> True")
    else:
        print(f"{digit} -> False")
