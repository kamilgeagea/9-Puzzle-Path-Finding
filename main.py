# Draw.io Link: https://app.diagrams.net/#LUntitled%20Diagram

from utility_functions import generate_puzzles, generate_output
from heuristics import h1, h2
from a_star import a_star
from id import iterative_deepening
from dfs import depth_first_search

# Number of puzzles
n = 20

# Dimensions
dimensions = 3

# Create puzzle
puzzles = generate_puzzles(n, dimensions)


# Initiate the results array for different algorithms
dfs_results = []
id_results = []
a_star_h1_results = []
a_star_h2_results = []


# Fill the array by computing each puzzle with each algorithm
for puzzle in puzzles:
    dfs_results.append(depth_first_search(puzzle, k=None))
    id_results.append(iterative_deepening(puzzle))
    a_star_h1_results.append(a_star(puzzle, h1))
    a_star_h2_results.append(a_star(puzzle, h2))


# Generate output file for DFS
generate_output("results/dfs.txt", dfs_results)
generate_output("results/id.txt", id_results)
generate_output("results/a_star_h1.txt", a_star_h1_results)
generate_output("results/a_star_h2.txt", a_star_h2_results)
