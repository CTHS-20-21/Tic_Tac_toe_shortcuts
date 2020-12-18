#generic code allow this to be reused
#create a list of strings from 1 to 9
board = []
for i in range(1,10):
    board.append(str(i))
print(board)

#since the code above can be any length - we need to set the print to accomodate it
breakrow = 3
board_print = "\n "
for b in range(0,len(board)):
    # for every time we hit breakrow, no vertical, and print the dash row
    #but no dash row at the end 
    if (b+1) % breakrow != 0:
        board_print += board[b]+ " | "
    elif (b+1) < len(board)-1:
        board_print += board[b]+"\n ---------\n "
    else:
        board_print += board[b]
board_print += "\n"
print(board_print)

def check_for_winner(board):
    
    # Check for a draw
    draw_flag = 0
    for i in range(len(board)):
        if board[i] is int: # can also use if board[i] != 'X' or board[i] != 'O'
            draw_flag = 1
    if draw_flag is 0:
        return "tie"
    
    # Check horizontals
    if (board[0] == board[1] and board[1] == board[2] and board[0] is not int):
        return board[0]
    if (board[3] == board[4] and board[4] == board[5] and board[3] is not int):
        return board[3]
    if (board[6] == board[7] and board[7] == board[8] and board[6] is not int):
        return oard[6]
    
    # Check verticals
    if (board[0] == board[3] and board[3] == board[6] and board[0] is not int):
        return board[0]
    if (board[1] == board[4] and board[4] == board[7] and board[1] is not int):
        return board[1]
    if (board[2] == board[5] and board[5] == board[8] and board[2] is not int):
        return board[2]
    
    # Check diagonals
    if (board[0] == board[4] and board[4] == board[8] and board[0] is not int):
        return board[0]
    if (board[2] == board[4] and board[4] == board[6] and board[2] is not int):
        return board[2]
    
    #check No one has won
    return "keep playing"
