loops = int(input())
letter_sum = 0

for i in range(loops):
    letter = str(input())
    letter_sum += ord(letter)
print(f"The sum equals: {letter_sum}")
