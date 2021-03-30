import time
from dfs import depth_first_search
from utility_functions import generate_puzzle, return_search_path

'''
Iterative Deepening - Will iterate over the limits and execute a DFS for each iteration
Arguments:
    - matrix: Initial NxN Matrix (start state)
Returns: Dictionary with the path (array of matrices from the start state to the goal) and execution time
'''


def iterative_deepening(matrix, time_limit=True):
    # Calculate the start time
    start_time = time.time()

    # Initialize k (max depth) to 1
    k = 1

    # Execute the algorithm until it returns a solution
    while True:
        # Check if the 60s limit has been exceeded
        if time.time() - start_time > 60 and time_limit:
            return {
                "data": "No solutions - Time exceeded",
                "execution_time": time.time() - start_time,
                "search_path": "No solutions"
            }

        # Execute DFS
        results = depth_first_search(matrix, k)

        # Check if the return type of the DFS is a List
        # If the return type is a list - the DFS returned the path that lead to the goal state - which means the algorithm has
        # succeeded
        if type(results["data"]) is list:
            finish_time = time.time() - start_time

            return {
                "data": results["data"],
                "execution_time": finish_time,
                "search_path": return_search_path(results["search_path"])
            }

        # Increment Max Depth for next iteration
        k = k + 1
