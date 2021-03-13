from utility_functions import generate_limit, up, down, left, right


class PuzzleNode:
    def __init__(self, parent, matrix, depth):
        self.parent = parent
        self.matrix = matrix
        self.depth = depth

    def generate_children(self):
        matrix = self.matrix
        new_depth = self.depth + 1

        limit = generate_limit(matrix)

        children = []

        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if i > 0:
                    puzzle = up(matrix, [i, j])
                    children.append(PuzzleNode(self, puzzle, new_depth))
                if i < limit:
                    puzzle = down(matrix, [i, j])
                    children.append(PuzzleNode(self, puzzle, new_depth))
                if j > 0:
                    puzzle = left(matrix, [i, j])
                    children.append(PuzzleNode(self, puzzle, new_depth))
                if j < limit:
                    puzzle = right(matrix, [i, j])
                    children.append(PuzzleNode(self, puzzle, new_depth))

        return children
