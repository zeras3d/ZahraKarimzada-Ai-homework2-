"""
Main game interface
"""

from game import *
from search import *

def play_game():
    print("Generalized Tic-Tac-Toe AI")
    
    m = int(input("Enter board size (m): ") or 3)
    k = int(input(f"Enter win condition (k-in-a-row, ≤{m}): ") or 3)
    
    state = initial_state(m, k)
    
    while not terminal(state):
        print_board(state)
        print(f"\nCurrent player: {player(state)}")
        
        if player(state) == 'X':
            # AI move
            if m == 3:
                _, move = minimax_ab(state)
            else:
                _, move = depth_limited_search(state, depth=4)
            
            state = result(state, move)
            print(f"AI plays: {move}")
        else:
            # Human move
            while True:
                try:
                    move = tuple(map(int, input("Enter your move (row col): ").split()))
                    if move in actions(state):
                        state = result(state, move)
                        break
                    else:
                        print("Invalid move! Try again.")
                except:
                    print("Please enter two numbers separated by space.")
    
    print_board(state)
    result_val = utility(state)
    if result_val == 1:
        print("X wins!")
    elif result_val == -1:
        print("O wins!")  
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
