board_list = ['#', '', '', '', '', '', '', '', '', '']


def clear_output():
    print('\n' * 100)


def display_board(board):
    """
this function should display a 3x3 board, with an index from 1-9
"""
    print(board[1] + ' |', board[2] + ' |', board[3])
    print(board[4] + ' |', board[5] + ' |', board[6])
    print(board[7] + ' |', board[8] + ' |', board[9])

    return board


test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(test_board)


def player_input():
    marker = ''
    # keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O': ")

    # assign player 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = "X"
    print(f'Player1 is {player1} and Player2 is {player2}')
    return (player1, player2)


player1_marker, player2_marker = player_input()


# player_input()

def place_marker(board, marker, position):
    while position not in range(1, 10):
        position = int(input('Please choose where you place your marker: '))
    else:
        board[position] = marker

    return board

place_marker(test_board, 'X', 10)
display_board(test_board)


