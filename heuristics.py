import numpy as np
from itertools import chain
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


# def h4(state):
#     # Get Matrix Dimensions
#     dimensions = len(state)

#     # Generate Goal
#     goal = generate_goal(dimensions)

#     # Initiate sum
#     sum = 0

#     # Loop through every element and compute distance with the goal coords
#     # Add the distance to the sum
#     for i in range(0, dimensions):
#         for j in range(0, dimensions):
#             element = state[i][j]
#             goal_element = get_coords(goal, element)

#             point1 = np.array(goal_element)
#             point2 = np.array((i, j))

#             sum += np.linalg.norm(point1-point2)

#     return sum


# def h3(state):
#     a = list(chain.from_iterable(state))

#     sum = 0

#     for i in range(0, len(a)):
#         for j in range(i+1, len(a)):
#             if a[i] > a[j]:
#                 sum += 1

#     return sum
