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
