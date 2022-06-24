starting_energy = int(input())
user_input = input()
battle_won = 0
end_game = False

while user_input != "End of battle":
    distance = int(user_input)
    if distance <= starting_energy:
        battle_won += 1
        starting_energy -= distance
        if battle_won % 3 == 0:
            starting_energy += battle_won
    elif distance > starting_energy:
        end_game = True
        print(f"Not enough energy! Game ends with {battle_won} won battles and {starting_energy} energy")
        break
    user_input = input()

if starting_energy >= 0 and end_game is False:
    print(f"Won battles: {battle_won}. Energy left: {starting_energy}")
