"""
Tic Tac Toe Player
"""
from copy import deepcopy
from random import choice 
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    ##### Assuming X starts first #####
    countX = 0
    countO = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == X:
                countX += 1
            if board[i][j] == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                ans.update({(i,j)})
    return ans

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    B = deepcopy(board)
    i = action[0]
    j = action[1]
    if B[i][j] != EMPTY:
        raise Exception
    else:
        B[i][j] = player(B)
    return B 

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    Winner = None
    if (board[0][0] == EMPTY) and (board[1][1] == EMPTY) and (board[2][2] == EMPTY):
        return Winner 

    for i in range(0,3):
        if (board[i][0] != EMPTY) and (board[i][0] == board[i][1] == board[i][2]):
            Winner = board[i][0]
            return Winner 
        if (board[0][i] != EMPTY) and (board[0][i] == board[1][i] == board[2][i] != EMPTY):
            Winner = board[0][i]
            return Winner

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        Winner = board[1][1]
        return Winner 
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        Winner = board[1][1]
        return Winner 

    return Winner 
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True 

    all_done = True  
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                all_done = False 
    return all_done

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1 
    elif w == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    B = deepcopy(board)
    a1 = actions(B)
    a2 = set()
    plyer = player(B)
    oppnt = opponent(plyer)

    while len(a1) >0:
        q = a1.pop()
        B[q[0]][q[1]] = plyer
        #print(B,winner(B),q,len(a1))
        if winner(B) == plyer:
            return q
        B[q[0]][q[1]] = EMPTY
        a2.update({q})

    while len(a2) > 0:
        q = a2.pop()
        B[q[0]][q[1]] = oppnt
        #print(B,winner(B),q,len(a1))
        if winner(B) == oppnt:
            return q
        B[q[0]][q[1]] = EMPTY
        a1.update({q})

    if (1,1) in a1:
        #print(q)
        return (1,1)

    www = choice(list(a1))
    return www

    raise NotImplementedError

def opponent(player):
    if player == X:
        return O
    if player == O:
        return X
