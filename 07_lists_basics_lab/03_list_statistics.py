loops = int(input())
positive = []
negative = []
count_positives = 0
sum_neg = 0

for i in range(loops):
    current = int(input())
    if current >= 0:
        positive.append(current)
        count_positives += 1
    else:
        negative.append(current)
        sum_neg += current

print(f"{positive}\n{negative}\nCount of positives: {count_positives}\nSum of negatives: {sum_neg}")
