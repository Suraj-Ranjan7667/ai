import numpy as np
import random
from time import sleep

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return list(zip(*np.where(board == 0)))

def random_place(board, player):
    board[random.choice(possibilities(board))] = player
    return board

def check_win(board, player):
    return any(all(board[i] == player) for i in range(3)) or \
           any(all(board[:, i] == player) for i in range(3)) or \
           all(board[i, i] == player for i in range(3)) or \
           all(board[i, 2 - i] == player for i in range(3))

def evaluate(board):
    for player in [1, 2]:
        if check_win(board, player):
            return player
    return -1 if np.all(board) else 0

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board); sleep(1)
    
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after {counter} move:\n{board}\n")
            sleep(1)
            counter += 1
            winner = evaluate(board)
            if winner: return f"Winner is: {winner}"

print(play_game())