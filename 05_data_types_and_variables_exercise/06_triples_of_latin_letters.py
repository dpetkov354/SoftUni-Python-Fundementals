num = int(input())
for i in range(0, num):
    char_one = chr(97 + i)
    for k in range(0, num):
        char_two = chr(97 + k)
        for j in range(0, num):
            char_three = chr(97 + j)
            print(f"{char_one}{char_two}{char_three}")
