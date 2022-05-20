
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")

    
# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    board_p1 = [[['-' for col in range(board_size)] for col in range(board_size)] for col in range(2)]
    board_p2 = [[['-' for col in range(board_size)] for col in range(board_size)] for col in range(2)]
    ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    ships_len = {'carrier' : 5, 'battleship' : 4, 'cruiser' : 3, 'submarine' : 3, 'destroyer' : 2}
    player_no = 0
    ships_to_be_placed = [[ship for ship in ships] for p in range(2)]
    #placement starts
    while player_no<2:
        #choosing the board
        if player_no == 0:
            board = board_p1
        elif player_no == 1:
            board = board_p2
        ships_already_placed = [[], []]
        while ships_to_be_placed[player_no] !=[]:       #checking if there any ships to place
            print_3d_list(board)
            print_ships_to_be_placed()
            for ship in ships_to_be_placed[player_no]: #remaining ships printed
                print_single_element(ship)
            print_empty_line()
            print_player_turn_to_place(player_no+1)
            print_to_place_ships()
            ship_input = input().strip().lower().split()
            ship_name = ship_input[0]

            try:
                x = int(ship_input[1]) #creating errors to check format
                x = int(ship_input[2])

                if int(ship_input[1]) in [i for i in range(1,11)] and int(ship_input[2]) in [i for i in range(1,11)]:       #is coordinates ok?
                    if ship_input[0] in [ship.lower() for ship in ships_to_be_placed[player_no]]:       #checking for the input ship
                        if ship_input[3].lower() == 'h': #horizontal ship
                            #does ship exceed the board?
                            if int(ship_input[1]) + ships_len[ship_input[0].lower()] - 1 < 11:
                                ship_input_as = int(ship_input[1]) - 1
                                #are there other ships in your life????
                                while board[player_no][int(ship_input[2]) - 1][ship_input_as] == '-':
                                    ship_input_as += 1
                                    #
                                    if ship_input_as == int(ship_input[1]) - 1 + ships_len[ship_input[0].lower()]:
                                        ship_input_as = int(ship_input[1]) - 1
                                        for x in range(ships_len[ship_input[0].lower()]):
                                            board[player_no][int(ship_input[2]) - 1][ship_input_as] = '#'       #placing it yeah :)
                                            ship_input_as += 1
                                        for shippy in ships_to_be_placed[player_no]:
                                            if shippy.lower() == ship_input[0].lower():         #storing the used ships
                                                ships_to_be_placed[player_no].remove(shippy)
                                                ships_already_placed[player_no].append(shippy.lower())
                                                break
                                        break
                                #how could you do this to me??? :(   (occupied)
                                else:
                                    for ship in ships:
                                        if ship_input[0] == ship.lower():
                                            print_ship_cannot_be_placed_occupied(ship)
                            #it does exceed sry :(
                            else:
                                for ship in ships:
                                    if ship_input[0] == ship.lower():
                                        print_ship_cannot_be_placed_outside(ship)
                        elif ship_input[3].lower() == 'v':          #vertical ship
                            # does ship exceed the board?
                            if int(ship_input[2]) + ships_len[ship_input[0].lower()] - 1 < 11:
                                ship_input_as = int(ship_input[2]) - 1
                                #are there other ships in your life????
                                while board[player_no][ship_input_as][int(ship_input[1]) - 1] == '-':
                                    ship_input_as += 1
                                    if ship_input_as == int(ship_input[2]) - 1 + ships_len[ship_input[0].lower()]:
                                        ship_input_as = int(ship_input[2]) - 1
                                        for x in range(ships_len[ship_input[0].lower()]):       #placing it yeah
                                            board[player_no][ship_input_as][int(ship_input[1]) - 1] = '#'
                                            ship_input_as += 1
                                        for shippy in ships_to_be_placed[player_no]:
                                            if shippy.lower() == ship_input[0].lower():         #storing the used ships
                                                ships_to_be_placed[player_no].remove(shippy)
                                                ships_already_placed[player_no].append(shippy.lower())
                                                break
                                        break
                                # how could you do this to me??? :(    (occupied)
                                else:
                                    for ship in ships:
                                        if ship_input[0] == ship.lower():
                                            print_ship_cannot_be_placed_occupied(ship)
                            # it does exceed sry :(
                            else:
                                for ship in ships:
                                    if ship_input[0] == ship.lower():
                                        print_ship_cannot_be_placed_outside(ship)

                        #wrong orientation
                        else:
                            print_incorrect_orientation()

                    elif ship_input[0] in ships_already_placed[player_no] and ship_input[0] in [ship.lower() for ship in ships]:        #if ship is already placed
                        try:
                            x = int(ship_input[1])      #checking for error in format again
                            y = int(ship_input[2])

                        except:
                            print_incorrect_input_format()

                        for ship in ships:
                            if ship_input[0] == ship.lower():
                                print_ship_is_already_placed(ship)
                    #wrong ship name
                    else:
                        print_incorrect_ship_name()
                #coordinates not ok :(
                else:
                    print_incorrect_coordinates()
            # format not cool :(
            except:
                print_incorrect_input_format()
        #when player finished the placement
        else:
            print_3d_list(board)
            y_n = '                                  '
            while y_n != 'n' or y_n != 'y':         #right answer
                print_confirm_placement()
                y_n = input().strip().lower()
                if y_n == 'y':      #player finished placement
                    player_no += 1
                    break
                elif y_n == 'n':
                    ships_to_be_placed[player_no] = [ship for ship in ships]
                    board[player_no] = [['-' for col in range(board_size)] for col in range(board_size)]
                    break
                else:       #wrong answer, asking again
                    continue




    #will sink some ships now :)
    player_no = 0
    current_player = player_no
    board = board_p1
    ships_not_gone = True
    board = board_p1
    other_board = board_p2
    while ships_not_gone:
        #finding the user
        if current_player == 0:
            other_player = 1

        else:
            other_player = 0
        print_3d_list(board)
        ships_not_gone = False
        # checking if any ships left
        for row in other_board[other_player]:
            if '#' in row:
                ships_not_gone = True
                break
        #checking if any ships left
        if ships_not_gone == False:
            continue        #game will finish if this 'continue' get processed

        print_player_turn_to_strike(current_player + 1)
        print_choose_target_coordinates()       #asking for target
        target_coordinates = input().strip().split()
        try:
            if len(target_coordinates) != 2:        #checking format
                print_incorrect_input_format()
                continue
            if int(target_coordinates[0]) in [i for i in range(1,11)] and int(target_coordinates[1]) in [i for i in range(1,11)]:       #checking the coordinates
                #checking if the strike was succesfull
                if other_board[other_player][int(target_coordinates[1])-1][int(target_coordinates[0])-1] == '#':        #it was successful obviously
                    board[other_player][int(target_coordinates[1])-1][int(target_coordinates[0])-1] = '!'
                    other_board[other_player][int(target_coordinates[1]) - 1][int(target_coordinates[0]) - 1] = '!'
                    print_hit()
                    continue


                elif other_board[other_player][int(target_coordinates[1])-1][int(target_coordinates[0])-1] == '!' or other_board[other_player][int(target_coordinates[1])-1][int(target_coordinates[0])-1] == 'O':
                    print_tile_already_struck()         #it hit but for the second time sry
                    continue
                elif other_board[other_player][int(target_coordinates[1])-1][int(target_coordinates[0])-1] == '-':      #ha ha missed
                    board[other_player][int(target_coordinates[1])-1][int(target_coordinates[0])-1] = 'O'
                    other_board[other_player][int(target_coordinates[1]) - 1][int(target_coordinates[0]) - 1] = 'O'
                    print_miss()
                    print_type_done_to_yield(other_player + 1)
                    done_not = input().strip().lower()
                    while done_not != 'done':       #misser passes the turn sry
                        print_type_done_to_yield(other_player+1)
                        done_not = input().strip().lower()
                    else:       #come on don't cry     (misser can't stand losing)     (wrong input)
                        temp1 = current_player
                        current_player = other_player
                        other_player = temp1
                        temp2 = board
                        board = other_board
                        other_board = temp2
                        continue

            else:       #coordinate not cool
                print_incorrect_coordinates()
        except:         #format not cool
            print_incorrect_input_format()

    else:       #congrats man u won this useless python game \-_-/
        print_player_won(current_player+1)
        print_thanks_for_playing()


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

