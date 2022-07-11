letters = {}
symbols = ''.join(s for s in input().split())
for letter in symbols:
    if letter not in letters.keys():  # not in letters
        letters[letter] = 0
    letters[letter] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")

# for key in letters.keys():
#    print(f"{key} -> {letters[key]}")
