import re


names_list = input()
pattern = r'(\b[A-Z][a-z]+ [A-Z][a-z]+\b)'

matches = re.findall(pattern, names_list)
print(' '.join(matches))
