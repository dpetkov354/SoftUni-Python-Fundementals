elements = list(input().split(" "))
loop = True
guess_count = 0

while loop:
    guess = input()
    guess_count += 1
    if guess == "end":
        loop = False
        if len(elements) > 0:
            print(f"Sorry you lose :(\n{' '.join(map(str, elements))}")
        break
    guess_list = list(map(int, guess.split(" ")))
    if guess_list[0] == guess_list[1] or guess_list[0] < 0 or guess_list[1] < 0 or guess_list[0] > (len(elements) - 1)\
            or guess_list[1] > (len(elements) - 1):
        print("Invalid input! Adding additional elements to the board")
        midpoint = len(elements) // 2
        penalty_element = f"-{guess_count}a"
        elements.insert(midpoint, penalty_element)
        elements.insert(midpoint, penalty_element)
        continue
    if elements[guess_list[0]] == elements[guess_list[1]]:
        print(f"Congrats! You have found matching elements - {elements[guess_list[0]]}!")
        remove_element = elements[guess_list[0]]
        elements.remove(remove_element)
        elements.remove(remove_element)
        if len(elements) == 0:
            print(f"You have won in {guess_count} turns!")
            while True:
                guess = input()
                guess_count += 1
                if guess == "end":
                    loop = False
                    break
    elif elements[guess_list[0]] != elements[guess_list[1]]:
        print("Try again!")
