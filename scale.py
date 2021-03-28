from a_star import a_star
from heuristics import h1, h2
from utility_functions import generate_puzzles, generate_output

# Number of puzzles
n = 1

# Generate 4x4 puzzles
puzzles4x4 = generate_puzzles(n, 4)

h1_4x4_results = []
h2_4x4_results = []

for puzzle in puzzles4x4:
    h1_4x4_results.append(a_star(puzzle, h1))
    h2_4x4_results.append(a_star(puzzle, h2))

generate_output("results/scale/h1_4x4.txt", h1_4x4_results)
generate_output("results/scale/h2_4x4.txt", h2_4x4_results)

# Generate 5x5 puzzles
puzzles5x5 = generate_puzzles(n, 5)

h1_5x5_results = []
h2_5x5_results = []

for puzzle in puzzles5x5:
    h1_5x5_results.append(a_star(puzzle, h1))
    h2_5x5_results.append(a_star(puzzle, h2))

generate_output("results/scale/h1_5x5.txt", h1_5x5_results)
generate_output("results/scale/h2_5x5.txt", h2_5x5_results)

# Generate 6x6 puzzles
puzzles6x6 = generate_puzzles(n, 6)

h1_6x6_results = []
h2_6x6_results = []

for puzzle in puzzles6x6:
    h1_6x6_results.append(a_star(puzzle, h1))
    h2_6x6_results.append(a_star(puzzle, h2))

generate_output("results/scale/h1_6x6.txt", h1_6x6_results)
generate_output("results/scale/h2_6x6.txt", h2_6x6_results)
