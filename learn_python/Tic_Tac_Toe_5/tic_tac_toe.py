#print out the board
def display_board(board):
    print('\n'*20)  #it's like clear the board from jupiter notebook
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])

#take a player input and assigned to x or 0
def player_input():
    marker=''
    while marker !='x' and marker !='0':
        marker=input("Player 1, choose x or 0: ")
    player1=marker
    if player1 == 'x':
        return ('x','0')
    else:
        return('o','x')

#assign the x or 0 to a specific position from the board (1-9)
def place_marker(board, marker, position):
    board[position]=marker

#possible combination to win
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#decide randomly which player go first
import random
def choose_first():
    if random.randint(0,1)==0:
        return "Player 2"
    else:
        return "Player 1"

#return a boolena indicator if a space from the board is available
def space_check(board, position):
    return board[position] == ' '

#check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#ask for player next position
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

#after the game is end, ask if the players want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#the functionality of the game 
print('Welcome to Tic Tac Toe!')
player_1_name=input("Player 1, what do you want us to call you:")
print("Player 1 will be assigned to "+player_1_name)
player_2_name=input("Player 2, what do you want us to call you:")
print("Player 2 will be assigned to "+player_2_name)
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! '+player_1_name+' won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! '+player_2_name+' won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break