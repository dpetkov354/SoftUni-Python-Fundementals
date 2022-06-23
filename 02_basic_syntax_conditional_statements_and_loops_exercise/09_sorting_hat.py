user_input = ""
sort = True
while user_input != "Welcome!" and sort:
    user_input = input()
    if user_input == "Welcome!":
        break
    elif user_input == "Voldemort":
        print("You must not speak of that name!")
        sort = False
        break
    elif len(user_input) < 5:
        print(f"{user_input} goes to Gryffindor.")
    elif len(user_input) == 5:
        print(f"{user_input} goes to Slytherin.")
    elif len(user_input) == 6:
        print(f"{user_input} goes to Ravenclaw.")
    elif len(user_input) > 6:
        print(f"{user_input} goes to Hufflepuff.")
if sort:
    print("Welcome to Hogwarts.")
