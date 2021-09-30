from Utils import create_grid, print_grid, count_blocks
from Node import Node
import pandas as pd
from time import time
from queue import PriorityQueue
from dataclasses import dataclass, field
import sys

max = sys.maxsize

@dataclass(order=True)
class PrioritizedItem:
    priority: float
    item: object = field()

def calc_manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def Astar(knowledge_grid, start, end, weight=1, flag=True, heuristic="manhattan"):
    grid_len = len(knowledge_grid)

    # Initialize a priority queue
    pQueue = PriorityQueue()
    pQueue.put(PrioritizedItem(0.0, start))
    closed_hash = {}    
    counter = 0

    while not pQueue.empty():
        # print(counter, len(pQueue.queue))
        if counter > 20000:
            return [None]

        counter+=1

        current = pQueue.get().item

        #Using dictionary instead of a list, to make retrival easier
        closed_hash[current.position] = True

        # Check if we have reached the goal, return the path
        if current == end:
            path = []
            while current != start:
                path.append(current.position)
                current = current.parent
            path.append(start.position)
            # Return reversed path
            return [path[::-1]]

        for n in current.get_neigbours(knowledge_grid):
            #check if neighbor is in closed set
            if n.position in closed_hash:
                continue
            #calculate heuristics for the neighbor
            if heuristic == "manhattan":
                n.h = calc_manhattan(n.position, [grid_len-1,grid_len-1])
            elif heuristic == "euclidean":
                n.h = calc_euclidean(n.position, [grid_len-1,grid_len-1])
            elif heuristic == "chebyshev":
                n.h = calc_chebyshev(n.position, [grid_len-1,grid_len-1])

            if flag:
                n.f = n.g + n.h*weight
                #check if node is in priority queue if yes does it have lower value?

                #add n to priority queue
                (x, y) = n.position
                if knowledge_grid[x][y] != 1:
                    pQueue.put(PrioritizedItem(float(n.f), n))

            #When using ASTAR to verify our solution consider undiscovered node's g to be infinity
            else:
                if knowledge_grid[n.position[0]][n.position[1]] ==  '-':
                    n.g = max
                n.f = n.g + n.h*weight
                #check if node is in priority queue if yes does it have lower value?

                #add n to priority queue
                (x, y) = n.position
                if knowledge_grid[x][y] != 1:
                    pQueue.put(PrioritizedItem(float(n.f), n))

    return [None]


def implement(matrix, knowledge, path):
    for itr in  range(1,len(path)):
        i = path[itr][0]
        j = path[itr][1]
        if matrix[i][j] == 1:
            knowledge[i][j] = 1
            return path[itr-1]
        if i+1<len(matrix):
            if matrix[i+1][j]==1:
                knowledge[i+1][j] = 1
            elif matrix[i+1][j] == 0:
                knowledge[i+1][j] = 0
        if j+1<len(matrix):
            if matrix[i][j+1]==1:
                knowledge[i][j+1] = 1
            elif matrix[i][j+1] == 0:
                knowledge[i][j+1] = 0
        if i-1>0:
            if matrix[i-1][j]==1:
                knowledge[i-1][j] = 1
            elif matrix[i-1][j]==0:
                knowledge[i-1][j] = 0
        if j-1>0: 
            if matrix[i][j-1]==1:
                knowledge[i][j-1] = 1
            elif matrix[i][j-1]==0:
                knowledge[i][j-1] = 0
    return path[len(path)-1]

def repeated(matrix, knowledge, start, end, cost, weight, heuristic="manhattan"):
    flag = False
    while True:
        res = Astar(knowledge, start, end, weight, heuristic)
        path = res[0]
        if path:
            last = implement(matrix, knowledge, path)
            cost = cost + path.index(last)

            last_Node = Node(last)
            if path[len(path)-1] == last:
                flag = True
                break
            start = last_Node
        else:
            break
    return (path,cost)

result = {
    "Trial" : [],
    "weight-1-Trajectory" : [],
    "weight-1-Shortest" : [],
    "weight-1-Time" : [],
    "weight-5-Trajectory" : [],
    "weight-5-Shortest" : [],
    "weight-5-Time" : [],
    "weight-15-Trajectory" : [],
    "weight-15-Shortest" : [],
    "weight-15-Time" : [],
}


for i in range(1,100):  
    grid_len = 101
    matrix = create_grid(grid_len, 0.20)

    result["Trial"].append(i)

    knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]

    # print("")
    # print_grid(matrix)
    # print("")

    start = Node()
    start.position = (0, 0)
    goal = Node()
    goal.position = (grid_len-1, grid_len-1)


    cost = 0
    weight = 1
    res = repeated(matrix, knowledge, start, goal, cost,  weight)
    print("path1:", res[0])
    print("cost1: ", res[1])
    result["weight-1-Trajectory"].append(res[1])


    # print("##############")
    cost = 0
    start_time = time()
    res = repeated(matrix, matrix, start, goal, cost, weight)
    end_time = time() - start_time
    result["weight-1-Time"].append(end_time)
    result["weight-1-Shortest"].append(res[1])


    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    ##############################################################################

    knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]

    weight = 5

    start = Node()
    start.position = (0, 0)
    goal = Node()
    goal.position = (grid_len-1, grid_len-1)

    cost = 0
    res = repeated(matrix, knowledge, start, goal, cost, weight)
    print("path2:", res[0])
    print("cost2:", res[1])
    result["weight-5-Trajectory"].append(res[1])

    # print("##############")
    cost = 0
    start_time = time()
    res = repeated(matrix, matrix, start, goal, cost, weight)
    end_time = time() - start_time
    result["weight-5-Time"].append(end_time)
    result["weight-5-Shortest"].append(res[1])

    ################################################################################

    knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]

    weight = 15

    start = Node()
    start.position = (0, 0)
    goal = Node()
    goal.position = (grid_len-1, grid_len-1)

    cost = 0
    res = repeated(matrix, knowledge, start, goal, cost, weight)
    print("path3:", res[0])
    print("cost3:", res[1])
    result["weight-15-Trajectory"].append(res[1])

    # print("##############")
    cost = 0
    start_time = time()
    res = repeated(matrix, matrix, start, goal, cost, weight)
    end_time = time() - start_time
    result["weight-15-Time"].append(end_time)
    result["weight-15-Shortest"].append(res[1])

data = pd.DataFrame(result)
data.to_csv("Question8.csv", index=False, encoding='utf-8')

#Final output
# print("Final Path", Astar(knowledge, start, goal))
