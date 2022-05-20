print('Welcome to the Tic Tac Toe Game')
print('The game needs two human players that will play in alternate turns')

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

winner = False

def start_game():
    playerx()

def playerx():
    global winner
    correct = False
    while correct == False:
        choice_player = input('Player (X), please choose your row number followed by the column number (e.g. 12)')
        row_choice = int(choice_player[0])
        column_choice = int(choice_player[1]) - 1
        if not isinstance(row_choice, int) or not isinstance(column_choice, int):
            print('The information provided is incorrect, please try again')
        else:
            correct = True
            print(correct)

    if row_choice == 1:
        row1[column_choice] = 'X'
    elif row_choice == 2:
        row2[column_choice] = 'X'
    elif row_choice == 3:
        row3[column_choice] = 'X'

    print(row1)
    print(row2)
    print(row3)

    if row1[0] == row2[0] == row3[0] == 'X':
        winner = True
    elif  row1[1] == row2[1] == row3[1] == 'X':
        winner = True
    elif  row1[2] == row2[2] == row3[2] == 'X':
        winner = True
    elif  row1[0] == row1[1] == row1[2] == 'X':
        winner = True
    elif  row2[0] == row2[1] == row2[2] == 'X':
        winner = True
    elif  row3[0] == row3[1] == row3[2] == 'X':
        winner = True
    elif  row1[0] == row2[1] == row3[2] == 'X':
        winner = True
    elif  row1[2] == row2[1] == row3[0] == 'X':
        winner = True
    
    if winner == True:
        return print('Player (X) is the winner!')

    playero()

def playero():
    global winner
    correct = False
    while correct == False:
        choice_player = input('Player (O), please choose your row number followed by the column number (e.g. 12)')
        row_choice = int(choice_player[0])
        column_choice = int(choice_player[1]) - 1
        if not isinstance(row_choice, int) or not isinstance(column_choice, int):
            print('The information provided is incorrect, please try again')
        else:
            correct = True

    if row_choice == 1:
        row1[column_choice] = 'O'
    elif row_choice == 2:
        row2[column_choice] = 'O'
    elif row_choice == 3:
        row3[column_choice] = 'O'

    print(row1)
    print(row2)
    print(row3)

    if row1[0] == row2[0] == row3[0] == 'O':
        winner = True
    elif  row1[1] == row2[1] == row3[1] == 'O':
        winner = True
    elif  row1[2] == row2[2] == row3[2] == 'O':
        winner = True
    elif  row1[0] == row1[1] == row1[2] == 'O':
        winner = True
    elif  row2[0] == row2[1] == row2[2] == 'O':
        winner = True
    elif  row3[0] == row3[1] == row3[2] == 'O':
        winner = True
    elif  row1[0] == row2[1] == row3[2] == 'O':
        winner = True
    elif  row1[2] == row2[1] == row3[0] == 'O':
        winner = True
    
    if winner == True:
        return print('Player (O) is the winner!')
        
    playerx()

start_game()