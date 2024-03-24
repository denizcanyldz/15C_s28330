import math

from square_generator.square_generator import SquareGenerator,InvalidRangeError,CubicGenerator

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
    cube_generator = CubicGenerator(3, 5)
    cubes_and_roots = cube_generator.generate_cubes()
    print(cubes_and_roots)
except InvalidRangeError as e:
    print(f"Error: {e}")