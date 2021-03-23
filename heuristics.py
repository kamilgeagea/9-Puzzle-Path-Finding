import numpy as np
from utility_functions import generate_goal, get_coords

'''
Heuristic that calculates the sum of the number of moves needed for each element to get to its goal coords
Arguments:
  - state: NxN Matrix
Returns: Number -> Sum of each element minimum moves needed to get to its goal coords
'''


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


'''
Heuristic that calculates the sum of the sum of the euclidian distance between an element and its goal position
Arguments:
  - state: NxN Matrix
Returns: Number -> Sum of each element minimum moves needed to get to its goal coords
'''


def h2(state):
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
            goal_element = get_coords(goal, element)

            point1 = np.array(goal_element)
            point2 = np.array((i, j))

            sum += np.linalg.norm(point1-point2)

    return sum
