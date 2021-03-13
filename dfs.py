import time
from PuzzleNode import PuzzleNode
from utility_functions import generate_puzzle, is_goal, in_puzzle_node_list, return_path


def depth_first_search(matrix, k):
    start_time = time.time()

    open = [PuzzleNode(None, matrix, 0)]
    closed = []

    while len(open) > 0:
        if time.time() - start_time > 60:
            return {
                "data": "No solutions - Time exceeded",
                "execution_time": time.time() - start_time
            }

        item = open.pop(0)
        closed.append(item)

        if is_goal(item.matrix):
            finish_time = time.time() - start_time

            return {
                "data": return_path(item),
                "execution_time": finish_time
            }

        if k is None or item.depth < k:
            children = item.generate_children()

            for child in children:
                if in_puzzle_node_list(child, closed) or in_puzzle_node_list(child, open):
                    pass
                else:
                    open.insert(0, child)

    finish_time = time.time() - start_time

    return {
        "data": "No solutions - Execution Time: ",
        "execution_time": finish_time
    }
