import numpy as np

def position_ant(M, S):     
    board = [M][M]
    count = 0
    for X in range (M):
        for Y in range (M):
            if(Y == M):
                count = count + 1
                board[X+1,Y]
            else:
                count = count + 1
                board[X,Y] = count
    print(board)

position_ant(4,10)
