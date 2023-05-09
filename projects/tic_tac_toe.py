# Import dependencies
from IPython.display import clear_output

# Create a default board
def board_reset():
    global header
    global row1
    global row2
    global row3
    header = " ___ ___ ___"
    row1 = ["|___","|___","|___","|"]
    row2 = ["|___","|___","|___","|"]
    row3 = ["|___","|___","|___","|\n"]
board_reset()

# Create function to display the board
def display_board(header, row1, row2, row3):
    print(header)
    print(''.join(row1))
    print(''.join(row2))
    print(''.join(row3))

# Create function to display the game title
def game_title():
    print("Welcome to TIC TAC TOE!")
    print("*"*23)

# Create function for the game
def new_game():
    turn = 1
    while turn <= 9:
        # Determine which player's turn it is and take input for desired square.
        if turn % 2 != 0:
            # Set player symbol
            player = 'X'
        else:
            # Set player symbol
            player = 'O'

        # Take user input for desired square and validate entry
        valid = False
        while valid == False:
            try:
                row, column = input(f"Player {player}, please enter your desired square (row, column): ").split(',')
            except ValueError:
                print("Invalid choice entry, please enter your desired square using numbers as 'row, square'")
                continue
            # Validate user input to ensure choice is both on the board and available for selection.            
            if 1 <= int(row) <= 3 and 1 <= int(column) <= 3:
                # Convert player input to integers for board updating
                row = int(row)
                column = int(column) - 1
                if row == 1:
                    if row1[column] == "|___":        
                        # Set player choice as valid and continue
                        valid = True
                elif row == 2:
                    if row2[column] == "|___":        
                        # Set player choice as valid and continue
                        valid = True
                elif row == 3:
                    if row3[column] == "|___":        
                        # Set player choice as valid and continue
                        valid = True
                else:
                    print("The selected square is already taken! Please enter your desired square.")
                    continue
            if valid == False:
                print("Please enter a valid row, choice for your turn")

        # Update board based on player selection
        if row == 1:
            row1[column] = f"|_{player}_"
        elif row == 2:
            row2[column] = f"|_{player}_"
        elif row == 3:
            row3[column] = f"|_{player}_"

        # Clear pervious output
        clear_output()
        # Display game title
        game_title()
        # Display choice of square
        print(f"Player {player} has selected row {row}, column {column+1}:")
        # Display updated board
        display_board(header, row1, row2, row3)

        # Check if either player has won the game
        if row1[0] != "|___" and row1[0] == row1[1] and row1[0] == row1[2]:
            print(f"Player {player} has won!")
            break
        if row2[0] != "|___" and row2[0] == row2[1] and row2[0] == row2[2]:
            print(f"Player {player} has won!")
            break
        if row3[0] != "|___" and row3[0] == row3[1] and row3[0] == row3[2]:
            print(f"Player {player} has won!")
            break
        if row1[0] != "|___" and row1[0] == row2[0] and row1[0] == row3[0]:
            print(f"Player {player} has won!")
            break
        if row1[1] != "|___" and row1[1] == row2[1] and row1[1] == row3[1]:
            print(f"Player {player} has won!")
            break
        if row1[2] != "|___" and row1[2] == row2[2] and row1[2] == row3[2]:
            print(f"Player {player} has won!")
            break
        if row1[0] != "|___" and row1[0] == row2[1] and row1[0] == row3[2]:
            print(f"Player {player} has won!")
            break
        if row1[2] != "|___" and row1[2] == row2[1] and row1[2] == row3[0]:
            print(f"Player {player} has won!")
            break

        # Iterate through the turns
        turn += 1

    # Check if the game has ended in a draw
    if turn == 10:
        print("The game has ended in a DRAW!")

    # Ask if the user would like to play again
    play_prompt = input("Do you want to play again? (y/n): ")
    if play_prompt.lower() == 'y':
        board_reset()
        new_game()
    elif play_prompt.lower() == 'n':
        print("Thanks for playing!")
        exit
    else:
        print("Thanks for playing!")
        exit

# Initialize game
def game_runner():
    play_prompt = input("Do you want to play TIC TAC TOE? (y/n): ")
    if play_prompt.lower() == 'y':
        board_reset()
        new_game()
    elif play_prompt.lower() == 'n':
        exit
    else:
        game_runner()

game_runner()