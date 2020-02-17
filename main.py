import random


num_pad = ['#',"1","2","3","4","5","6","7","8","9"]
input_board = [' ']*10
current_game = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']




def print_board(key):
    #Create board with array elements as spaces, and using "|" for alignment
    clear_output()
    print(key[1]+"|"+key[2]+"|"+key[3])
    print("-|-|-")
    print(key[4] + "|" + key[5] + "|" + key[6])
    print("-|-|-")
    print(key[7] + "|" + key[8] + "|" + key[9])

def clear_output():
    #Create the impression that its one dynamic board. One on the screen at a time
    print("\n"*50)



def get_user_input():
    selection = ''
    #Keep prompting till X or O is selected
    while selection!='X' and selection!='O':
        selection = input("Player 1, please select either 'X' or 'O'").upper()
        player_1=selection
    if player_1 =="X":
        player_2 = "O"
    else:
        player_2 = "X"
    return (player_1,player_2)





def place_selection(board,selection,position):
    #Place marker of selected position on board
    board[position]=selection


def full_board_check(board):
    for space in range(0,10):
        if space_check(board,space):
            return False
        #BOARD IS FULL IF TRUE
        return True


def win_check(board,mark):
    #Check for same values in rows// #Check for same values in columns// #Check for same values in both diagonals
    return  (board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark)  or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)


def space_check(board,position):
    return board[position] == " "



def play_first():
    flip = random.randint(0,1)
    if flip==0:
        return "Player 1"
    else:
        return "Player 2"


def player_choice(board,player):
    player_position = 0
    while player_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,player_position):
        player_position = int(input(f"{player}, please enter a position from 1-9 "))
    return player_position


def replay():
    choice = input("Do you want to play again? Enter Yes or No").lower()
    return choice == 'yes'




print("Welcome to Tic Tac Toe")

while True:

    #PLAY THE GAME

    #SET EVERYTHING UP(BOARD, WHO'S FIRST, CHOOSE MARKERS X,O)
    current_game = [' ']*10
    player1_marker, player2_marker = get_user_input()

    turn = play_first()
    print(turn + " will go first")
    game_on = False
    play_game = input("Ready to play? Yes or no").lower()

    if play_game == "yes":
        game_on = True
    else:
        game_on = False



    #GAME PLAY
    while game_on:

    ##PLAYER 1 TURN
        if turn == 'Player 1':
            #display the board
            print_board(current_game)
            #pick a position
            position = player_choice(current_game,turn)
            #place marker on board
            place_selection(current_game,player1_marker,position)

            #check if they won
            if win_check(current_game,player1_marker):
                print_board(current_game)
                print("\nPLAYER 1 HAS WON THE GAME! WOO HOO!")
                game_on = False

            #check if a tie
            elif full_board_check(current_game):
                print_board(current_game)
                print("\nIT'S A TIE. WHAT A SHAME :(")
                game_on = False
            # If no win and no tie, then next player's turn
            else:
                turn = 'Player 2'



    ##PLAYER 2 TURN
        if turn == 'Player 2':
            print_board(current_game)

            position = player_choice(current_game,turn)

            place_selection(current_game, player2_marker, position)


            if win_check(current_game, player2_marker):
                print_board(current_game)
                print("\nPLAYER 2 HAS WON THE GAME! WOO HOO!")
                game_on = False


            elif full_board_check(current_game):
                print_board(current_game)
                print("\nIT'S A TIE. WHAT A SHAME :(")
                game_on = False

            else:
                turn = 'Player 1'



    if not replay():
        break



