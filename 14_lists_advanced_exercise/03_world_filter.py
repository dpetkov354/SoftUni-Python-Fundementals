word_list = input().split()
filter_list = [word for word in word_list if len(word) % 2 == 0]
print(*filter_list, sep='\n')
