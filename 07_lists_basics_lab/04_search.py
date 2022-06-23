loops = int(input())
word = str(input())

strings = []
finished = []

for i in range(loops):
    current = str(input())
    strings.append(current)
print(strings)

for j in range(len(strings) -1, -1, -1):
    elem = strings[j]
    if word not in elem:
        strings.remove(elem)

print(strings)
