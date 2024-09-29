# simple implementation of tic-tac-toe game in python
# GitHub JawadMohammedK
import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):# the win conditions is the places that have a pattern of three values and must be the same
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    if " " not in board:
        return "Tie"
    return False

def computer_move(board):
    possible_moves = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(possible_moves)
    board[move]= "O"

def game():
    board = [" "] * 9
    while True:
        print_board(board)
        move = input("Enter your move (1-9): ")
        if board[int(move) - 1] != " ":
            print("invalid move, please try again.")
            continue
        board[int(move) - 1] = "X"
        result = check_win(board)
        if result:
            print_board(board)
            if result == "Tie":
                print("its a Tie")
            else:
                print(f"\33[34m{result}\33[0m wins!")
            break
        computer_move(board)
        result = check_win(board)
        if result:
            print_board(board)
            if result == "Tie":
                print("it's a tie")
            else:
                print(f"\33[31m{result}\33[0m wins!")
            break

game()