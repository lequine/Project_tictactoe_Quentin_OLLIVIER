"""
Tic Tac Toe Player
"""
import random
import math
from copy import deepcopy


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
    res=0 #nbr of empty
    for x in board:
        for y in x :
            if  y == EMPTY:
                res=res+1
    if res%2==1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res=[]
    for x in board:
        for y in x :
            if y == EMPTY:
                res.append((board.index(x),x.index(y)))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    """b=board.copy()
    if b[action[0]][action[1]]==EMPTY:
        b[action[0]][action[1]]=player(b)
    else:
        print('not empty')#a finir plus tard !!!!!!!!!!!!!"""
        
    i = action[0]
    j = action[1]
        
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
        raise Exception('Result function given an invalid board position for action: ')
    elif board[i][j] != EMPTY:
        raise Exception('Result function tried to perform invalid action on occupaied tile: ')

    board_copy = deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    tab=[[board[0][0],board[0][1],board[0][2]],
         [board[1][0],board[1][1],board[1][2]],
         [board[2][0],board[2][1],board[2][2]],
         [board[0][0],board[1][0],board[2][0]],
         [board[0][1],board[1][1],board[2][1]],
         [board[0][2],board[1][2],board[2][2]],
         [board[0][0],board[1][1],board[2][2]],
         [board[2][0],board[1][1],board[0][2]]]
    
    if [X,X,X] in tab :
        return X
    elif [O,O,O] in tab:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
    """

    global actions_explored
    actions_explored = 0

    def max_player(board, best_min = 10):

      global actions_explored

      if terminal(board):
        return (utility(board), None)

      value = -10
      best_action = None


      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        if best_min <= value:
          break

        actions_explored += 1
        min_player_result = min_player(result(board, action), value)
        if min_player_result[0] > value:
          best_action = action
          value = min_player_result[0]

      return (value, best_action)


    def min_player(board, best_max = -10):

      global actions_explored

      if terminal(board):
        return (utility(board), None)

      value = 10
      best_action = None

      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        if best_max >= value:
          break

        actions_explored += 1
        max_player_result = max_player(result(board, action), value)
        if max_player_result[0] < value:
          best_action = action
          value = max_player_result[0]

      return (value, best_action)


    if terminal(board):
      return None

    if player(board) == 'X':
      print('AI is exploring possible actions...')
      best_move = max_player(board)[1]
      print('Actions explored by AI: ', actions_explored)
      return best_move
    else:
      print('AI is exploring possible actions...')
      best_move = min_player(board)[1]
      print('Actions explored by AI: ', actions_explored)
      return best_move
        
