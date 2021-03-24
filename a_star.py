import time
from utility_functions import is_goal, return_path, generate_children, in_list

'''
A* Algorithm
Arguments:
  - state: initial state (tuple) representing NxN Matrix
  - heuristic: heuristic function we want to apply
Returns: Dictionary with the path (array of matrices from the start state to the goal) and execution time
'''


def a_star(state, heuristic):
    # Initializing start time
    start_time = time.time()

    # Initializing open (to-do list) and closed (completed list) lists
    # The open array is initialized wiht a tuple indicating the depth (0) of the current node, the parent (None) of the node,
    # the initial matrix state, and f(n) = g(n) + h(n) with g -> depth of state and h -> heuristic of
    open = [(0, None, state)]
    closed = []

    # Algorithm runs while the open list has elements
    while len(open) > 0:
        # Check if the 60s mark is exceeded - if yes return "no solutions"
        if time.time() - start_time > 60:
            return {
                "data": "No solutions - Time exceeded",
                "execution_time": time.time() - start_time
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
                "search_path": closed
            }

        # If the state is not the goal state - generate children
        children = generate_children(node)

        # Generate f(n) for children
        children = [(depth, parent, state, depth + heuristic(state))
                    for (depth, parent, state) in children]

        # Verify for each child that it is not already in open or closed list
        # If child passes condition, add to open list
        for child in children:
            if in_list(child, closed) or in_list(child, open):
                pass
            else:
                open.insert(0, child)

        # Sort the open list based on f(n)
        open.sort(key=lambda x: x[3])

    # If open is empty and goal state not found, the algorithm didn't find the solution

    # Calculate execution time
    finish_time = time.time() - start_time

    # Return execution time and "no solutions" message
    return {
        "data": "No solutions - Execution Time: ",
        "execution_time": finish_time
    }
