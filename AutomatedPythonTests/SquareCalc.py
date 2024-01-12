# Creates a class that makes square objects given a side length
# Used for testing in the test files
class Square:
    def __init__(self, length) -> None:
        self.length = length

    # Gets area of the square
    def area(self):
        return self.length * self.length

    # Gets perimeter of the square
    def perimeter(self):
        return self.length * 4