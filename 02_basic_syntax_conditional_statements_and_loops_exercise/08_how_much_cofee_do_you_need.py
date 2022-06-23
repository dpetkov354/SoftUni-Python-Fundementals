user_input = ""
coffee_count = 0
while user_input != "END":
    user_input = input()
    if user_input == "coding" or user_input == "cat" or user_input == "dog" or user_input == "movie":
        coffee_count += 1
    elif user_input == "CODING" or user_input == "CAT" or user_input == "DOG" or user_input == "MOVIE":
        coffee_count += 2
    else:
        continue
if coffee_count <= 5:
    print(coffee_count)
else:
    print("You need extra sleep")
