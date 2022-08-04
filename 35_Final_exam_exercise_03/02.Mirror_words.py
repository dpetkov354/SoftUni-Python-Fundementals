import re


def mirror_words():
    data = input()
    pattern = r'(\@|\#)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)'
    result = re.finditer(pattern, data)
    results = []
    reverse_results = []

    for item in result:
        info = item.group()
        results.append(info)

    if len(results) == 0:
        print("No word pairs found!")

    elif len(results) > 0:
        print(f"{len(results)} word pairs found!")

    for pair in results:
        pair = pair.replace("##", "|")
        pair = pair.replace("@@", "|")
        middle_mark = int((len(pair) - 1) / 2)
        start = pair[:middle_mark]
        end = pair[middle_mark+1:][::-1]
        if start == end:
            pair = pair.replace("|", " <=> ")
            pair = pair.replace("#", "")
            pair = pair.replace("@", "")
            reverse_results.append(pair)

    if len(reverse_results) == 0:
        print("No mirror words!")

    elif len(reverse_results) > 0:
        print("The mirror words are:")
        print(', '.join(reverse_results))


mirror_words()
