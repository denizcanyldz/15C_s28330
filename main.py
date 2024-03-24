import math

squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print(squares)


# Task 2: Functions
def square_list(start, end):
    squares1 = []
    for y in range(start, end + 1):
        squares1.append(y ** 2)
    return squares1


# Let's write an example
example = square_list(2, 6)
print(example)

# Task 3: Classes and Task 4: Libraries
class SquareGenerator:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def generate_squares_and_roots(self):
        squares_and_roots = []
        for x in range(self.start, self.end + 1):
            square = x**2
            square_root = math.sqrt(square)
            squares_and_roots.append((square, square_root))
        return squares_and_roots

# Let's write an example
example = SquareGenerator(3,5)
generator = example.generate_squares_and_roots()
print("Squares and Square Roots:")
for square, root in generator:
    print(f"Number: {square}, Square Root: {root:.2f}")



