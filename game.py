"""
Tic-Tac-Toe game engine for m×m board with k-in-a-row win condition
"""

def initial_state(m=3, k=3):
    return {
        'board': [[' ' for _ in range(m)] for _ in range(m)],
        'm': m,
        'k': k,
        'current_player': 'X'
    }

def player(state):
    return state['current_player']

def actions(state):
    m = state['m']
    board = state['board']
    return [(i, j) for i in range(m) for j in range(m) if board[i][j] == ' ']

def result(state, action):
    i, j = action
    new_state = {
        'board': [row[:] for row in state['board']],
        'm': state['m'],
        'k': state['k'],
        'current_player': 'O' if state['current_player'] == 'X' else 'X'
    }
    new_state['board'][i][j] = state['current_player']
    return new_state

def winner(state):
    board = state['board']
    m, k = state['m'], state['k']
    
    # Check rows
    for i in range(m):
        for j in range(m - k + 1):
            if board[i][j] != ' ' and all(board[i][j] == board[i][j + step] for step in range(k)):
                return board[i][j]
    
    # Check columns
    for i in range(m - k + 1):
        for j in range(m):
            if board[i][j] != ' ' and all(board[i][j] == board[i + step][j] for step in range(k)):
                return board[i][j]
    
    # Check diagonals
    for i in range(m - k + 1):
        for j in range(m - k + 1):
            if board[i][j] != ' ' and all(board[i][j] == board[i + step][j + step] for step in range(k)):
                return board[i][j]
    
    # Check anti-diagonals
    for i in range(m - k + 1):
        for j in range(k - 1, m):
            if board[i][j] != ' ' and all(board[i][j] == board[i + step][j - step] for step in range(k)):
                return board[i][j]
    
    return None

def terminal(state):
    if winner(state) is not None:
        return True
    return all(cell != ' ' for row in state['board'] for cell in row)

def utility(state):
    win = winner(state)
    if win == 'X': return 1
    if win == 'O': return -1
    return 0

def print_board(state):
    board = state['board']
    m = state['m']
    print("   " + " ".join(str(i) for i in range(m)))
    for i in range(m):
        print(f"{i}  " + " | ".join(board[i]))
        if i < m - 1:
            print("  " + "---" * (m + 1))
