import time
from utility_functions import generate_puzzle, is_goal, in_list, generate_children, return_path, return_search_path

'''
Depth First Search Algorithm on a Matrix
Arguments:
    - matrix: Initial NxN Matrix (start state)
    - k: depth limit (integer)
Returns: Dictionary with the path (array of matrices from the start state to the goal) and execution time
'''


def depth_first_search(state, k):
    # Initializing start time
    start_time = time.time()

    # Initializing open (to-do list) and closed (completed list) lists
    # The open array is initialized wiht a tuple indicating the depth (0) of the current node, the parent (None) of the node
    # and the initial matrix state
    open = [(0, None, state)]
    closed = []

    # Algorithm runs while the open list has elements
    while len(open) > 0:
        # Check if the 60s mark is exceeded - if yes return "no solutions"
        if time.time() - start_time > 60:
            return {
                "data": "No solutions - Time exceeded",
                "execution_time": time.time() - start_time,
                "search_path": "No solutions"
            }

        # Retrieve the first item in the open list, remove it, and add it to the closed list to mark it as done
        node = open.pop(0)
        closed.append(node)

        # Check if the state of the node is equal to the goal - if yes the algorithm has reached its objective
        if is_goal(node[2]):
            # Calculate the finish time of the algorithm
            finish_time = time.time() - start_time

            # Return the path that lead to the solution and the execution time
            return {
                "data": return_path(node),
                "execution_time": finish_time,
                "search_path": return_search_path(closed)
            }

        # If the state is not the goal state - go deeper into the branch

        # Check if limit depth is reached, if not generate children of current node
        if k is None or node[0] < k:
            children = generate_children(node)

            # Verify for each child that it is not already in open or closed list
            for child in children:
                if in_list(child, closed) or in_list(child, open):
                    pass
                else:
                    open.insert(0, child)

    # If open is empty and goal state not found, the algorithm didn't find the solution

    # Calculate execution time
    finish_time = time.time() - start_time

    # Return execution time and "no solutions" message
    return {
        "data": "No solutions - Execution Time: ",
        "execution_time": finish_time,
        "search_path": "No solutions"
    }
