from dfs import depth_first_search
from id import iterative_deepening
from a_star import a_star
from heuristics import h1, h2
from utility_functions import print_output

# Insert puzzles in array

puzzles = [
    ((4, 6, 1), (2, 3, 7), (9, 5, 8)),
    ((5, 7, 3), (1, 6, 8), (9, 2, 4))
]

for idx, puzzle in enumerate(puzzles):
    dfs_result = depth_first_search(puzzle, k=None)
    id_result = iterative_deepening(puzzle)
    a_star_h1 = a_star(puzzle, h1)
    a_star_h2 = a_star(puzzle, h2)

    print_output("DFS - Puzzle " + str(idx+1), dfs_result)
    print_output("ID - Puzzle " + str(idx+1), id_result)
    print_output("A* h1 - Puzzle " + str(idx+1), a_star_h1)
    print_output("A* h2 - Puzzle " + str(idx+1), a_star_h2)
