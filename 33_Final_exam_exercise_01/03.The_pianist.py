def store_piano_information(piano_dictionary, number):
    for _ in range(number):
        data = input().split('|')
        piece = data[0]
        composer = data[1]
        key = data[2]

        piano_dictionary[piece] = [composer, key]

    return piano_dictionary


def special_commands(piano_dictionary):
    while True:
        command = input()

        if command == 'Stop':
            break

        command = command.split('|')
        current_command = command[0]
        current_piece = command[1]

        if current_command == 'Add':

            piece = current_piece
            composer = command[2]
            key = command[3]

            if piece not in piano_dictionary:
                piano_dictionary[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")

            else:
                print(f"{piece} is already in the collection!")

        elif current_command == 'Remove':
            piece = current_piece

            if piece in piano_dictionary:
                del piano_dictionary[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        elif current_command == 'ChangeKey':
            piece = current_piece
            new_key = command[2]

            if piece in piano_dictionary:
                piano_dictionary[piece][1] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

    return piano_dictionary


def additional_print_function(cars_dictionary):
    for i in cars_dictionary:
        piece = i
        composer = cars_dictionary[i][0]
        key = cars_dictionary[i][1]

        print(f"{piece} -> Composer: {composer}, Key: {key}")


def piano_pieces(number):
    piano_dictionary = {}

    store_piano_information(piano_dictionary, number)
    special_commands(piano_dictionary)
    additional_print_function(piano_dictionary)


n = int(input())
piano_pieces(n)
