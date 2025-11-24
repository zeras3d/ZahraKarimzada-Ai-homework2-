"""
Test cases for the Tic-Tac-Toe AI
"""

from game import *
from search import *

def test_3x3_optimal():
    """Test that AI plays optimally on 3x3 board"""
    print("Testing 3x3 optimal play...")
    state = initial_state(3, 3)
    
    # First move should be center or corner
    _, move1 = minimax(state)
    _, move2 = minimax_ab(state)
    assert move1 == move2, "Minimax and Alpha-Beta should agree"
    print("✓ 3x3 optimal test passed")

def test_win_detection():
    """Test win condition detection"""
    print("Testing win detection...")
    
    # Test horizontal win
    state = initial_state(3, 3)
    state['board'] = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
    assert winner(state) == 'X', "Horizontal win not detected"
    
    # Test vertical win  
    state['board'] = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']]
    assert winner(state) == 'X', "Vertical win not detected"
    
    print("✓ Win detection tests passed")

def test_alpha_beta_equivalence():
    """Test that Alpha-Beta returns same moves as Minimax"""
    print("Testing Alpha-Beta equivalence...")
    
    test_states = [
        [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']],
        [['X', ' ', 'O'], [' ', 'X', ' '], ['O', ' ', ' ']]
    ]
    
    for board in test_states:
        state = initial_state(3, 3)
        state['board'] = [row[:] for row in board]
        
        _, move1 = minimax(state)
        _, move2 = minimax_ab(state)
        assert move1 == move2, f"Moves differ: {move1} vs {move2}"
    
    print("✓ Alpha-Beta equivalence tests passed")

def run_all_tests():
    test_win_detection()
    test_3x3_optimal() 
    test_alpha_beta_equivalence()
    print("🎉 All tests passed!")

if __name__ == "__main__":
    run_all_tests()
