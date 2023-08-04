# %%

from IPython.display import clear_output


def display_board(board):

    for i in range(3):
        print(board[(i*3)+0:(i*3)+3])

    print("\n\n")


def choose_position(already_chosen=[]):

    print("Please input a number between 1 and 9 to choose where to put your sign")

    allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    valid_input = False

    while not valid_input:

        position = input()

        if not position.isdigit():
            print("You need to input a digit number, you moron")
            continue # Return to the beginning of the while loop to get a new value

        position = int(position)

        if position not in allowed_values:
            print("The number needs to be between 1 and 9, are you stupid or what?")
            continue # Return to the beginning of the while loop to get a new value
        elif position in already_chosen:
            print("You cannot choose a position that was already chosen, you cheater")
        else:
            valid_input = True
            clear_output()
            print("Nice, you made it! Here's the updated board")


    return position


def has_won(player_choices):

    won = False

    winning_conditions = [ #All possible winning conditions of the game
        set([1, 2, 3]),
        set([4, 5, 6]),
        set([7, 8, 9]),
        set([1, 4, 7]),
        set([2, 5, 8]),
        set([3, 6, 9]),
        set([1, 5, 9]),
        set([3, 5, 7]),
    ]

    for item in winning_conditions:
        if item.issubset(player_choices):
            won = True

    return won

def play_more():

    valid_input = False
    print("\n\nSince you had so much fun, do you want to play one more game? Please enter 'Y' if yes or 'N' if not. It's case sensitive" )

    while not valid_input:
        yes_or_no = input()

        if yes_or_no != 'Y' and yes_or_no != 'N':
            print("I told you to either write 'Y' or 'N'! Do you think you're funny ignoring me \nand writing whatever you want? You're the ones losing time playing this stupid game")
            continue
        else:
            valid_input = True
            clear_output()
            if yes_or_no == 'Y':
                print("\nOh really, you want to play again? You don't have a very exciting life, do you?")
            elif yes_or_no == 'N':
                print("\nFuck off, I didn't enjoy playing with you either")

    return yes_or_no == 'Y'

# %%

### Initialize variables

initial_board = [" "]*9
map_board = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]
keep_playing = True

# %%
### Actual game

clear_output()

print("Welcome to Eugenio's tic-tac-toe, the game from which brands like Ubisoft, Epic games, \nand many more got inspired for their work! We're free minds, so this is available for free.")
print("\nThis game is played in two players, one turn each. One person will put 'X' on the board, \nthe other player will put 'O'. \n\nTo select where you want to put your sign you'll indicate a position on the board with a number.")
print("\nPlayer 1 will be putting 'X', player 2 will be putting 'O'. If you don't like it, suck it up.")
print("\n")

# Here one game starts

while keep_playing:



    game_won = False
    gaming_board = initial_board.copy()
    player_1 = []
    player_2 = []
    already_chosen = []

    print("Here's your empty board you'll be playing with:")
    display_board(gaming_board)

    print("\nAnd here's the mapping, showing which number corresponds to which position")
    display_board(map_board)

    while not game_won:

        print("Player 1 ('X') playing")
        # Let the user choose a position to put their sign
        chosen_position = choose_position(already_chosen=already_chosen)
        
        # Update board, player choices, and available positions. Also check if the game is won
        player_1.append(chosen_position)
        already_chosen.append(chosen_position)
        gaming_board[chosen_position-1] = 'X'

        display_board(gaming_board)

        print("\nAnd here's a reminder of the mapping, since I know you're slow")
        display_board(map_board)

        if has_won(player_choices=player_1):
            print("Player 1 has won!!! Player 2, it's very hard to lose (not tie) at this game, reconsider your life choices")
            game_won = True
            break

        if len(already_chosen) == 9:
            print("The game finished with a very exciting tie! What a surprise! It seems none of you is excessively retarded")
            break

        print("Player 2 ('O') playing")
        chosen_position = choose_position(already_chosen=already_chosen)

        # Update board, player choices, and available positions. Also check if the game is won
        player_2.append(chosen_position)
        already_chosen.append(chosen_position)
        gaming_board[chosen_position-1] = 'O'

        display_board(gaming_board)
        print("\nAnd here's a reminder of the mapping, since I know you're slow")
        display_board(map_board)

        if has_won(player_choices=player_2):
            print("Player 2 has won!!! Player 1, it's very hard to lose (not tie) at this game, reconsider your life choices")
            game_won = True
            break


        

    keep_playing = play_more()
