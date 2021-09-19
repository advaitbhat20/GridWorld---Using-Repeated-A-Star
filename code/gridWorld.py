import numpy as np
# import pandas as pd
import random

def create_grid(n):
    matrix = [ [ 0 for i in range(n) ] for j in range(n) ]
    print(matrix)

    p = 0.75
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0) or (i==n-1 and j==n-1):
                matrix[i][j] = 0
            else:
                prob = random.uniform(0, 1)
                print(prob)
                if prob >= p:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
    return matrix

def print_grid(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")

matrix = create_grid(5)
print_grid(matrix)