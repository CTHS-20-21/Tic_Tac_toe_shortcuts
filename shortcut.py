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
