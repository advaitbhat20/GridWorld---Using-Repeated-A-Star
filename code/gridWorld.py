import numpy as np
# import pandas as pd
import random
import math

def create_grid(n):
    matrix = [ [ 0 for i in range(n) ] for j in range(n) ]

    p = 0.75
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0) or (i==n-1 and j==n-1):
                matrix[i][j] = 0
            else:
                prob = random.uniform(0, 1)
                if prob >= p:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
    return matrix

def print_grid(matrix):
    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")

    print("")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(calc_chebyshev([i,j], [n-1,n-1]), end=" ")
        print("")

def calc_manhattan(a,b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def calc_euclidean(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def calc_chebyshev(a,b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

matrix = create_grid(5)
print_grid(matrix)