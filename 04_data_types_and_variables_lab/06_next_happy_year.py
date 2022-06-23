year = int(input())

for i in range(year + 1, 99999999999999999999):
    str_year = str(i)
    zero_count = 0
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    seven_count = 0
    eight_count = 0
    nine_count = 0
    for j in str_year:
        if j == "0":
            zero_count += 1
        elif j == "1":
            one_count += 1
        elif j == "2":
            two_count += 1
        elif j == "3":
            three_count += 1
        elif j == "4":
            four_count += 1
        elif j == "5":
            five_count += 1
        elif j == "6":
            six_count += 1
        elif j == "7":
            seven_count += 1
        elif j == "8":
            eight_count += 1
        elif j == "9":
            nine_count += 1
    if zero_count > 1 or one_count > 1 or two_count > 1 or three_count > 1 or four_count > 1 or five_count > 1 or six_count > 1 or seven_count > 1 or eight_count > 1 or nine_count > 1:
        continue
    else:
        print(str_year)
        break
