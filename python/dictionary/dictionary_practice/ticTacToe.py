theBoard = {
        'top_L': 'O', 'top_M': 'O', 'top_R': 'O', 
        'mid_L': 'X', 'mid_M': 'X', 'mid_R': ' ', 
        'low_L': ' ', 'low_M': ' ', 'low_R': 'X'
        }
def printBoard(board) :
    print(board['top_L'] + ' | ' + board['top_M'] + ' | ' + board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + ' | ' + board['mid_M'] + ' | ' + board['mid_R'])
    print('-+-+-')
    print(board['low_L'] + ' | ' + board['low_M'] + ' | ' + board['low_R'])

printBoard(theBoard)

