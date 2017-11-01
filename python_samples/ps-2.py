"""

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
"""
import  math
class Factorial:
    def fact(self,x):
        if x == 0:
            return 1
        return x * fact(x - 1 )


if __name__ == '__main__':


