import re


def easter_eggs():
    data = input()
    pattern = r'((\@|\#){1,})([a-z]{3,})((\@|\#){1,})((\W+)*)(\/{1,})(\d+)(\/{1,})'
    result = re.finditer(pattern, data)
    for egg in result:
        letters = []
        digits = []
        word = egg.group()
        for char in word:
            if char.isalpha():
                letters.append(char)

            elif char.isdigit():
                digits.append(char)

        color = "".join(letters)
        amount = "".join(digits)
        print(f"You found {amount} {color} eggs!")


easter_eggs()
