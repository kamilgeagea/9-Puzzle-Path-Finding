import time
from PuzzleNode import PuzzleNode
from utility_functions import generate_puzzle, is_goal, in_puzzle_node_list


def depth_first_search(matrix):
    start_time = time.time()

    open = [PuzzleNode(None, matrix, 0)]
    closed = []

    while len(open) > 0:
        if time.time() - start_time > 60:
            return "No solutions - Time exceeded"

        item = open.pop(0)
        closed.append(item)

        if is_goal(item.matrix):
            finish_time = time.time() - start_time
            print("Algorithm Done - Execution Time: " + str(finish_time))

            return "Path found"

        children = item.generate_children()

        for child in children:
            if in_puzzle_node_list(child, closed) or in_puzzle_node_list(child, open):
                pass
            else:
                open.insert(0, child)

    finish_time = time.time() - start_time

    return "No solutions - Execution Time: " + str(finish_time)


puzzle = generate_puzzle(2)

print(depth_first_search(puzzle))
