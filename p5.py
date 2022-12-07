import math

def minimax(tree, depth): 
    max_turn = bool(depth % 2) 
    for _ in range(depth): 
        zipped = zip(tree[::2], tree[1::2]) 
        if max_turn: 
            tree = [max(a, b) for a, b in zipped] # max player 
        else:  
            tree = [min(a, b) for a, b in zipped] # min player 
        max_turn = not max_turn # swapping turns 
    return tree[0]

A = [3, 5, 2, 9, 12, 5, 23, 23] 
depth = math.ceil(math.log(len(A), 2)) 
print(f"Result = {minimax(A, depth)}")