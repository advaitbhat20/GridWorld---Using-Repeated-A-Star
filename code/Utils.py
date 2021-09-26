import random
import threading
import math

#creating a randomized grid world
def create_grid(n, p):
    matrix = [ [ 0 for i in range(n) ] for j in range(n) ]
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0) or (i==n-1 and j==n-1):
                matrix[i][j] = 0
            else:
                prob = random.uniform(0, 1)
                if prob >= p:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1
    return matrix

#print the gridworld/knowledge
def print_grid(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")

def count_blocks(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count+=1
    return count

def calc_manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def calc_euclidean(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def calc_chebyshev(a,b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))