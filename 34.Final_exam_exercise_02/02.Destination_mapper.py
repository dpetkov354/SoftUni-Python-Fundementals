import re


def emoji_detector():
    data = input()
    pattern = r'(\=|\/)[A-Z][A-Za-z]{2,}(\1)'
    result = re.finditer(pattern, data)
    results = []
    points = 0

    for item in result:
        info = item.group()
        info = info.replace("=", "")
        info = info.replace("/", "")
        results.append(info)

    for location in results:
        points += len(location)

    print(f"Destinations: {', '.join(results)}")
    print(f"Travel Points: {points}")


emoji_detector()
