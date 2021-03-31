# COMP472-Assignment 2
COMP 472 - Assignment 2 - The S Puzzle

# Puzzle Description
The S-Puzzle is a type of Sliding-tiles puzzle played on a n-by-n grid, with numbers occupying each individual cell. In the S-Puzzle, there is are no spaces; all n^2 tiles are occupied by a number from 1 - n^2. The game is played by swapping any two adjacent tiles, where adjacency is defined grid-wise (diagonal tiles are not adjacent) and does not wrap around. Like in the original Sliding Tiles puzzle, the goal of the S-Puzzle is to arrange the numbers in ascending order.


### Solution  
The final solution should look as follows:
```
[1,2,3
 4,5,6
 7,8,9]
 ```

## Getting Started
**Step 1:** Open a new project on Pycharm (Make sure you have **Python Version 3.8** installed on your computer).\
**Step 2:** Navigate to Pycharm settings

       > (Mac OS: Pycharm -> Preferences -> Project -> Python Interpretor -> "+")
       
       > (Windows OS: File -> Settings -> Project -> Python Interpretor -> "+")
       
**Step 3:** Install the following packages: 

       > numpy

**Step 4:** Clone Project

       > Import this project from Version Control
       
**Step 5:** Generate a new n x n Puzzle 

      > # In Main.py, Change the value of n to the desired number of puzzles:
      > n = 20 by default

      > # Next, Select Dimensions of puzzle, by default, 3x3 Puzzle is created
      > dimensions = 3

### Import Usage:
Ensure the following Imports are in Main.py File:
```
from dfs import depth_first_search
from id import iterative_deepening
from a_star import a_star
from heuristics import h1, h2
from utility_functions import generate_puzzles, generate_output

```

## Overall code process and code snippets
**Code Process:\
Step 1: Create Depth First Search Function:**
```
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
```

**Step 2: Create Iterative Deepening Function:**
```
def iterative_deepening(matrix):
    # Calculate the start time
    start_time = time.time()

    # Initialize k (max depth) to 1
    k = 1

    # Execute the algorithm until it returns a solution
    while True:
        # Check if the 60s limit has been exceeded
        if time.time() - start_time > 60:
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
```

**Step 3: Define Heuristic Functions to be used in A_Star Algorithm:**

**H1- Manhattan Distance**
      > Calculates Sum of the number of moves for each element to reach its goal state.
```
def h1(state):
    # Get Matrix Dimensions
    dimensions = len(state)

    # Generate Goal
    goal = generate_goal(dimensions)

    # Initiate sum
    sum = 0

    # Loop through every element and compute distance with the goal coords
    # Add the distance to the sum
    for i in range(0, dimensions):
        for j in range(0, dimensions):
            element = state[i][j]
            (goal_i, goal_j) = get_coords(goal, element)

            sum += abs(i - goal_i) + abs(j - goal_j)

    return sum
```

**H2- Weighted Manhattan Distance**
      > Calculates Sum of the number of moves for each element to reach its goal state and includes an importance factor based on the distance of the goal state from the closest corner.

<p align="center">
<img width="398" src="https://user-images.githubusercontent.com/55751464/112889559-c7bc2f80-90a3-11eb-97c1-9bbed2f56398.png">
</p>

```
def h2(state):
    # Get Matrix Dimensions
    dimensions = len(state)

    # Compute n
    n = dimensions - 1

    # Generate Goal
    goal = generate_goal(dimensions)

    # Initiate sum
    sum = 0

    # Define the coordinates of the 4 corners
    corners = ((0, 0), (0, n), (n, 0), (n, n))

    for i in range(0, dimensions):
        for j in range(0, dimensions):
            element = state[i][j]
            goal_element = get_coords(goal, element)

            closest_corner = ((0, 0), float("inf"))
            for k in corners:
                distance = abs(k[0] - goal_element[0]) + \
                    abs(k[1] - goal_element[1])
                if distance < closest_corner[1]:
                    closest_corner = (k, distance)

            importance = n - closest_corner[1]

            distance_to_goal = abs(
                i - goal_element[0]) + abs(j - goal_element[1])

            sum += importance * distance_to_goal

    return sum
```

**Step 4: Run the DFS, ID, and A_Star (with h1 and h2) on the generated puzzle:**
```
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

```

**Step 5: Output Results to respective file:**
```
generate_output("results/dfs.txt", dfs_results)
generate_output("results/id.txt", id_results)
generate_output("results/a_star_h1.txt", a_star_h1_results)
generate_output("results/a_star_h2.txt", a_star_h2_results)
```

## Get Help
To get help or ask questions, Please Contact any of the following students: 
 - **Full Name:** Kamil Geagea\
   **Student ID:** 40052432\
   **Github Username:** kamilgeagea\
   **Email Address:** kamilgeagea8199@gmail.com
   
 - **Full Name:** Marjana Upama\
   **Student ID:** 40058393\
   **Github Username:** Marjanaupama\
   **Email Address:** zana.zinly@gmail.com
   
 - **Full Name:** JC Manikis\
   **Student ID:** 26884466\
   **Github Username:** jmanikis\
   **Email Address:** jmanikis@icloud.com
   
 - **Full Name:** Mair Elbaz\
   **Student ID:** 40004558\
   **Github Username:** mairsarmy32\
   **Email Address:** mairelbaz552@hotmail.com
