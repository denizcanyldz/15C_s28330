import math

from square_generator import SquareGenerator, InvalidRangeError

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

# Let's write an example
try:
    example = SquareGenerator(3,5)
except InvalidRangeError as e:
    print(f"Error: {e}")

generator = example.generate_squares_and_roots()
print("Squares and Square Roots:")
for square, root in generator:
    print(f"Number: {square}, Square Root: {root:.2f}")


