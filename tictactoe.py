import random

def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board=['#','X','O','X','O','X','O','X','O','X']

def player_input():
    '''
    OUTPUT = (Player 1 marker,Player 2 marker)
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1:Chooose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, mark):

    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or(board[7] == board[8] == board[9] == mark) or(board[7] == board[4] == board[1] == mark) or(board[2] == board[5] == board[8] == mark) or (board[9] == board[6] == board[3] == mark) or(board[1] == board[5] == board[9] == mark)or (board[7] == board[5] == board[3] == mark)

def choose_first(flip=None):

    flip == random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    # BOARD IS FULL IF WE RETURN TRUE

    return True

def player_choice(board):
    global position
    position = None
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position

def replay():

    choice = input("Play again? Yes or No: ").upper()

    return choice == 'YES'

print('Welcome to TIC TAC TOE')

while True:

    #PLAY THE GAME

    the_board = [' ']*10
    player1_marker,player2_marker=player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Ready to play? y or n : ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn =='Player 1':

            display_board(the_board)
            position = player_choice(the_board)

            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON THE GAME !!!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)

            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON THE GAME !!!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
                    

                    
            
        
