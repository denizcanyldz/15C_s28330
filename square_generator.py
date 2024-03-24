import math


class SquareGenerator:
    def __init__(self,start,end):
        if end < start:
            raise InvalidRangeError("End of range must be greater than or equal to the start.")
        self.start = start
        self.end = end

    def generate_squares_and_roots(self):
        squares_and_roots = []
        for x in range(self.start, self.end + 1):
            square = x**2
            square_root = math.sqrt(square)
            squares_and_roots.append((square, square_root))
        return squares_and_roots


class InvalidRangeError(Exception):
    pass
