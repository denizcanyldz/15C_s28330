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

