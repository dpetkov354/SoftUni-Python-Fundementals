loops_start = int(input())
loops_finish = int(input())
string = ""

for i in range(loops_start, loops_finish + 1):
    letter = chr(i)
    string += str(letter)
    string += str(" ")
print(string)
