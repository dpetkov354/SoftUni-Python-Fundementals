loops = int(input())

not_finished = []
finished = []

for i in range(loops):
    current = int(input())
    not_finished.append(current)

word = input()

for i in not_finished:
    if word == "even":
        if i % 2 == 0 or i == 0:
            finished.append(i)
    elif word == "odd":
        if i % 2 != 0 and i != 0:
            finished.append(i)
    elif word == "positive":
        if i >= 0:
            finished.append(i)
    elif word == "negative":
        if i < 0:
            finished.append(i)

print(finished)
