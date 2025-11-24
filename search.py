"""
Minimax and Alpha-Beta search algorithms
"""

def minimax(state):
    if terminal(state):
        return utility(state), None
    
    current_player = player(state)
    best_move = None
    
    if current_player == 'X':  # Maximizing
        value = -float('inf')
        for action in actions(state):
            new_value, _ = minimax(result(state, action))
            if new_value > value:
                value = new_value
                best_move = action
        return value, best_move
    else:  # Minimizing
        value = float('inf')
        for action in actions(state):
            new_value, _ = minimax(result(state, action))
            if new_value < value:
                value = new_value
                best_move = action
        return value, best_move

def minimax_ab(state, alpha=-float('inf'), beta=float('inf')):
    if terminal(state):
        return utility(state), None
    
    current_player = player(state)
    best_move = None
    
    if current_player == 'X':  # Maximizing
        value = -float('inf')
        for action in actions(state):
            new_value, _ = minimax_ab(result(state, action), alpha, beta)
            if new_value > value:
                value = new_value
                best_move = action
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_move
    else:  # Minimizing
        value = float('inf')
        for action in actions(state):
            new_value, _ = minimax_ab(result(state, action), alpha, beta)
            if new_value < value:
                value = new_value
                best_move = action
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move

def evaluate(state):
    """Simple heuristic evaluation for larger boards"""
    win = winner(state)
    if win == 'X': return 100
    if win == 'O': return -100
    
    # Count potential lines
    score = 0
    # Simple center control
    m = state['m']
    center = m // 2
    if state['board'][center][center] == 'X':
        score += 10
    elif state['board'][center][center] == 'O':
        score -= 10
    
    return score

def depth_limited_search(state, depth=3, eval_fn=evaluate):
    if terminal(state) or depth == 0:
        return eval_fn(state), None
    
    current_player = player(state)
    best_move = None
    
    if current_player == 'X':  # Maximizing
        value = -float('inf')
        for action in actions(state):
            new_value, _ = depth_limited_search(result(state, action), depth-1, eval_fn)
            if new_value > value:
                value = new_value
                best_move = action
        return value, best_move
    else:  # Minimizing
        value = float('inf')
        for action in actions(state):
            new_value, _ = depth_limited_search(result(state, action), depth-1, eval_fn)
            if new_value < value:
                value = new_value
                best_move = action
        return value, best_move
