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

# Task 3: Classes
class SquareGenerator:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def generate_square(self):
        squares3 = []
        for z in range(self.start,self.end +1):
            squares3.append(z**2)
        return squares3

# Let's write an example
example = SquareGenerator(3,5)
print(example.generate_square())