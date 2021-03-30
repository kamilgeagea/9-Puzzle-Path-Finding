from random import shuffle
import numpy as np

'''
Convert a Tuple to a List or a List to a Tuple
Arguments:
  - tuple_or_list: Either a List to be converted to a Tuple or vice-versa
  - inverse: If True, will convert a List to a Tuple
Returns: List or Tuple
'''


def tuple_to_list(tuple_or_list, inverse=False):
    if not inverse:
        return [list(i) for i in tuple_or_list]
    else:
        return tuple(tuple(i) for i in tuple_or_list)


'''
Swap two elements in a Matrix
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
  - coords1: Coordinates of the first element we want to swap e.g. [0,0]
  - coords2: Coordinates of the second element we want to swap e.g. [0,1]
Returns: NxN Matrix
Throws: Index out of range error
'''


def swap(matrix, coords1, coords2):
    # Extracting the coords
    [i1, j1] = coords1
    [i2, j2] = coords2

    # Convert tuple to List
    matrix = tuple_to_list(matrix)

    temp = matrix[i1][j1]
    matrix[i1][j1] = matrix[i2][j2]
    matrix[i2][j2] = temp

    # Convert back to Tuple
    return tuple_to_list(matrix, inverse=True)


'''
Swap with the element above
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
  - coords: The coordinates of the item we want to swap e.g. [0.1]
Returns: NxN Matrix
Throws: Index out of range error
'''


def up(matrix, coords):
    # Extracting the coords
    [i, j] = coords
    i1 = i - 1  # (i1, j) will be the element above

    return swap(matrix, coords, [i1, j])


'''
Swap with the element to the left
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
  - coords: The coordinates of the item we want to swap e.g. [0.1]
Returns: NxN Matrix
Throws: Index out of range error
'''


def left(matrix, coords):
    # Extracting the coords
    [i, j] = coords
    j1 = j - 1  # (i1, j) will be the element to the left

    return swap(matrix, coords, [i, j1])


'''
Swap with the element to the right
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
  - coords: The coordinates of the item we want to swap e.g. [0.1]
Returns: NxN Matrix
Throws: Index out of range error
'''


def right(matrix, coords):
    # Extracting the coords
    [i, j] = coords
    j1 = j + 1  # (i1, j) will be the element to the right

    return swap(matrix, coords, [i, j1])


'''
Swap with the element below
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
  - coords: The coordinates of the item we want to swap e.g. [0.1]
Returns: NxN Matrix
Throws: Index out of range error
'''


def down(matrix, coords):
    # Extracting the coords
    [i, j] = coords
    i1 = i + 1  # (i1, j) will be the element below

    return swap(matrix, coords, [i1, j])


'''
Generates random N x N puzzle
Arguments:
  - dimensions: Dimensions of Matrix e.g. 3 -> 3x3
  - do_shuffle: Whether the puzzle shuffles
Returns: N x N Matrix
'''


def generate_puzzle(dimensions, do_shuffle=True):
    # Create new List of N dimensions
    numbers = np.array([i for i in range(1, dimensions**2 + 1)])
    if do_shuffle:
        shuffle(numbers)  # Shuffle the List
    # Reshape the flatlist into a N x N Matrix and convert it to a Tuple
    return tuple_to_list(numbers.reshape((dimensions, dimensions)), inverse=True)


'''
Generates n random N x N puzzles
Arguments:
  - n: Number of puzzles to be generated
  - dimensions: Dimensions of Matrix e.g. 3 -> 3x3
Returns: List of n N x N Matrix
'''


def generate_puzzles(n, dimensions):
    puzzles = []

    # Generate n puzzles
    for i in range(n):
        puzzles.append(generate_puzzle(dimensions))

    return puzzles


'''
Generates goal N x N puzzle (Ordered Puzzle)
Arguments:
  - dimensions: Dimensions of Matrix e.g. 3 -> 3x3
Returns: N x N Matrix
'''


def generate_goal(dimensions):
    return generate_puzzle(dimensions, do_shuffle=False)


'''
Generates the index limit of a Matrix -> The limit index before a row / column goes out of range
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
Returns: Number
'''


def generate_limit(matrix):
    return len(matrix) - 1


'''
Returns whether the matrix has reach the goal or not
Arguments:
  - matrix: NxN Matrix e.g. ((1,2,3),(4,5,6),(7,8,9))
Returns: Boolean
'''


def is_goal(state):
    dimensions = len(state)
    goal = generate_goal(dimensions)

    return state == goal


'''
Checks if a Node is contained in a list
Arguments:
  - node: Tuple e.g. (depth, parent, state)
  - node_list: List of Tuples e.g. [(depth, parent, state), (depth, parent, state)]
Returns: Boolean
'''


def in_list(state, state_list):
    for element in state_list:
        if state[2] == element[2]:
            return True

    return False


'''
Generates a List of tuple (children state) by making every possible move from a current state
Arguments:
  - node: Tuple e.g. (depth, parent, state)
Returns: List of Tuples e.g. [(depth, parent, state), (depth, parent, state)]
'''


def generate_children(state):
    matrix = state[2]
    new_depth = state[0] + 1

    limit = generate_limit(matrix)

    children = []

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if i < limit:
                new_state = down(matrix, [i, j])
                children.append((new_depth, state, new_state))
            if j < limit:
                new_state = right(matrix, [i, j])
                children.append((new_depth, state, new_state))

    return children


'''
Returns the path of a State
Arguments:
  - state: Instance of State (Tuple)
Returns: List of State instances -> NxN Matrices
'''


def return_path(state):
    path = []

    while state is not None:
        path.insert(0, state[2])
        state = state[1]

    return path


'''
Returns the states of the search path
Arguments:
  - nodes: Array of nodes -> [(depth, parent, state)]
Returns: List of State instances -> NxN Matrices
'''


def return_search_path(nodes):
    search_path = []

    for node in nodes:
        search_path.append(node[2])

    return search_path


'''
Returns the coords (row, col) of an element in an NxN Matrix
Arguments:
  - matrix: NxN Matrix (tuple)
  - element: Any
Returns: Tuple (row, col) indicating the coords of the element
'''


def get_coords(matrix, element):
    for row in range(0, len(matrix)):
        for col, ele in enumerate(matrix[row]):
            if ele == element:
                return (row, col)


'''
Returns the statistics related to an array of results from a specific algorithm
Arguments:
  - results: Array of Results -> [{"execution_time": double, "data": array, "search_path": array}]
Returns: Dictionary: { "total_execution_time": double,
        "total_search_path": double,
        "total_solution_path": double,
        "total_no_solution": double,
        "avg_execution_time": double,
        "avg_no_solution": double,
        "avg_solution_path": double,
        "avg_search_path": double }
'''


def generate_stats(results):
    total_results = len(results)

    total_execution_time = 0
    total_search_path = 0
    total_solution_path = 0
    total_no_solution = 0

    success_count = 0

    for result in results:
        if "No solutions" in result["data"]:
            total_no_solution += 1
            total_execution_time += result["execution_time"]
        else:
            success_count += 1
            total_execution_time += result["execution_time"]
            total_search_path += len(result["search_path"])
            total_solution_path += len(result["data"])

    avg_execution_time = total_execution_time / total_results
    avg_no_solution = total_no_solution / total_results
    if success_count == 0:
        avg_solution_path = 0
        avg_search_path = 0
    else:
        avg_solution_path = total_solution_path / success_count
        avg_search_path = total_search_path / success_count

    return {
        "total_execution_time": total_execution_time,
        "total_search_path": total_search_path,
        "total_solution_path": total_solution_path,
        "total_no_solution": total_no_solution,
        "avg_execution_time": avg_execution_time,
        "avg_no_solution": avg_no_solution,
        "avg_solution_path": avg_solution_path,
        "avg_search_path": avg_search_path
    }


'''
Function that takes a file name and an array of results, and outputs them in a file
Arguments:
  - filename: String
  - results: Array of Results -> [{"execution_time": double, "data": array, "search_path": array}]
Returns: void
'''


def generate_output(filename, results):
    # Generate statistics related to the results
    stats = generate_stats(results)

    with open(filename, mode="w") as f:
        # print("Statistics: \n", file=f)

        print("Total Execution Time: " +
              str(stats["total_execution_time"]) + "\n", file=f)
        print("Total Search Path: " +
              str(stats["total_search_path"]) + "\n", file=f)
        print("Total Solution Path: " +
              str(stats["total_solution_path"]) + "\n", file=f)
        print("Total No Solutions: " +
              str(stats["total_no_solution"]) + "\n", file=f)
        print("Average Execution Time: " +
              str(stats["avg_execution_time"]) + "\n", file=f)
        print("Average Search Path: " +
              str(stats["avg_search_path"]) + "\n", file=f)
        print("Average Solution Path: " +
              str(stats["avg_solution_path"]) + "\n", file=f)
        print("Average No Solutions: " +
              str(stats["avg_no_solution"]) + "\n", file=f)

        print("\n\n\n", file=f)

        for idx, result in enumerate(results):
            print("=== Puzzle " + str(idx+1) + " ===\n", file=f)
            print("Puzzle: " + str(result["data"][0]) + "\n", file=f)
            print("Execution Time: " +
                  str(result["execution_time"]) + "\n", file=f)
            print("Search Path: " +
                  str(result["search_path"]) + "\n", file=f)
            print("Solution Path: " +
                  str(result["data"]) + "\n", file=f)

            print("\n", file=f)


'''
Prints Results of Algorithms
Arguments:
  - title: String
  - result: dictionary: {"execution_time": double, "data": array, "search_path": array}
Returns: void
'''


def print_output(title, result):
    print(title + "\n")
    print("Execution Time: " + str(result["execution_time"]) + "\n")
    print("Search Path: " + str(result["search_path"]) + "\n")
    print("Solution Path: " + str(result["data"]) + "\n")
    print("\n")
