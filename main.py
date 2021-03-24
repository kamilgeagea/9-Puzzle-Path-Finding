from dfs import depth_first_search
from id import iterative_deepening
from a_star import a_star
from heuristics import h1, h2, h3, h4
from utility_functions import generate_puzzle

print("\n\n")

# Create 2x2 puzzle

# puzzle2x2 = generate_puzzle(2)

# # Apply Depth-First-Search on 2x2 puzzle
# dfs2x2 = depth_first_search(puzzle2x2, k=None)
# print("===== Depth-First-Search - 2x2 Matrix =====\n")
# print("Path: " + str(dfs2x2["data"]))
# print("Search Path: " + str(dfs2x2["search_path"]))
# print("Execution time - " + str(dfs2x2["execution_time"]) + " seconds\n\n")

# # Apply Iterative Deepening on 2x2 puzzle
# id2x2 = iterative_deepening(puzzle2x2)
# print("===== Iterarive-Deepening - 2x2 Matrix =====\n")
# print("Path: " + str(id2x2["data"]))
# print("Search Path: " + str(id2x2["search_path"]))
# print("Execution time - " + str(id2x2["execution_time"]) + " seconds\n\n")

# # Apply A* Algorithm on 2x2 puzzle
# as2x2 = a_star(puzzle2x2, h1)
# print("===== A-Star - 2x2 Matrix =====\n")
# print("Path: " + str(as2x2["data"]))
# print("Search Path: " + str(as2x2["search_path"]))
# print("Execution time - " + str(as2x2["execution_time"]) + " seconds\n\n")

# Create 3x3 puzzle
puzzle3x3 = generate_puzzle(5)

# # Apply Depth-First-Search on 3x3 puzzle
# dfs3x3 = depth_first_search(puzzle3x3, k=None)
# print("===== Depth-First-Search - 3x3 Matrix =====\n")
# print("Path: " + str(dfs3x3["data"]))
# print("Search Path: " + str(dfs3x3["search_path"]))
# print("Execution time - " + str(dfs3x3["execution_time"]) + " seconds\n\n")

# # Apply Iterative Deepening on 3x3 puzzle
# id3x3 = iterative_deepening(puzzle3x3)
# print("===== Iterarive-Deepening - 3x3 Matrix =====\n")
# print("Path: " + str(id3x3["data"]))
# print("Search Path: " + str(id3x3["search_path"]))
# print("Execution time - " + str(id3x3["execution_time"]) + " seconds\n\n")

# # # Apply A* Algorithm on 3x3 puzzle
as3x3 = a_star(puzzle3x3, h1)
print("===== A-Star - 3x3 Matrix =====\n")
print("Path: " + str(as3x3["data"]))
# print("Search Path: " + str(as3x3["search_path"]))
print("Execution time h1 - " + str(as3x3["execution_time"]) + " seconds\n\n")

# Apply A* Algorithm on 3x3 puzzle
# as3x3 = a_star(puzzle3x3, h4)
# print("===== A-Star - 3x3 Matrix =====\n")
# print("Path: " + str(as3x3["data"]))
# # print("Search Path: " + str(as3x3["search_path"]))
# print("Execution time h4 - " + str(as3x3["execution_time"]) + " seconds\n\n")
