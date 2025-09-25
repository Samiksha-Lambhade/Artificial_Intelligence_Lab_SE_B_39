def alpha_beta(node, depth, alpha, beta, maximizingPlayer, values, index=0):
    # Base case: depth is 0 or node is terminal (leaf)
    if depth == 0 or index >= len(values):
        return values[index]

    if maximizingPlayer:
        value = float('-inf')
        for i in range(2):  # Assume binary tree (2 children)
            child_index = index * 2 + i
            val = alpha_beta(node * 2 + i, depth - 1, alpha, beta, False, values, child_index)
            value = max(value, val)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cut-off
        return value
    else:
        value = float('inf')
        for i in range(2):  # Assume binary tree (2 children)
            child_index = index * 2 + i
            val = alpha_beta(node * 2 + i, depth - 1, alpha, beta, True, values, child_index)
            value = min(value, val)
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value


# Sample game tree represented by leaf node values
# Tree depth = 3, so number of leaves = 2^3 = 8
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Heuristic values at leaves

depth = 3  # Levels in the game tree
alpha = float('-inf')
beta = float('inf')
maximizingPlayer = True  # Start with MAX player

# Start from root node (index 0)
optimal_value = alpha_beta(0, depth, alpha, beta, maximizingPlayer, values)

print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

