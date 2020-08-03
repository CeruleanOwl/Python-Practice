'''Global Variables'''
#Set the winner
winner = None
#Set game Activity
game_active = True
#Set default player
current_player = 'X'



#board
board = ['-' ,'-' ,'-' ,'-' ,'-' ,'-' ,'-' ,'-' ,'-']
#diplay board function
def display_board():
    for i in range(len(board)):
        if ((i+1) % 3):
            print(board[i] ,end=' | ')
        else:
            print(board[i])

#handle turn
def handle_turn(player):
    #Allowed inputs
    input_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(player + '\'s turn.')
    
    #Request input
    position = input('Please select your position on the board: 1 - 9 \n')
    
    #checks if input fits parameters of game
    valid = False
    while not valid:
        while position not in input_options:
            position = input('[Invalid Input]Please select your position on the board: 1 - 9 \n')
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print('You can\'t go there, go again')

    board[position] = player

    display_board()

#check the rows
def check_rows():
    #set global variable
    global game_active

    #check if any rows have win condition
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    #Ends game if win
    if row1 or row2 or row3:
        game_active = False
    
    #return winnner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    
#checks the columns
def check_columns():
    #set global game_active
    global game_active

    #check if any columns have win condition
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    #End game if win
    if column1 or column2 or column3:
        game_active = False

    #return winner (X or O)
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

#checks for win condition on diagonals 
def check_diags():
    #set global game_active
    global game_active

    #check if any diags have win condition
    diagL = board[0] == board[4] == board[8] != '-'
    diagR = board[2] == board[4] == board[6] != '-'

    #Eng game if win
    if diagL or diagR:
        game_active = False

    #return winner (X or O)
    if diagL or diagR:
        return board[4]

    
#check if game is won
def check_for_winner():
    #Assign the global variable
    global winner
    #check row
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diag
    diag_winner = check_diags()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        #There was no win
        winner = None

#check if draw
def check_if_draw():
    #call global variable
    global game_active

    if '-' not in board:
        game_active = False

#check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_draw()

#switch player
def switch_player():
    #call global variable
    global current_player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

#game logic
def play_game():
    #display the initial board
    display_board()

    while game_active:
        handle_turn(current_player)

        check_if_game_over()

        switch_player()
    #print winner statement
    if winner == 'X':
        print('X is the winner!')
    elif winner == 'O':
        print('O is the winner!')
    
    #print draw statement
    if winner == None:
        print('This game was a draw.')


play_game()