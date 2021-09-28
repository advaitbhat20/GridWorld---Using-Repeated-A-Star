from Utils import create_grid, print_grid, count_blocks
from Node import Node
from Astar import Astar
from Exceution import repeated
import pandas as pd
from time import time

result = {
    "Dimension":[],
    "Probability": [],
    # "Matrix": [],
    "No_of_blocks":[],
    "Density": [],
    "Manhattan_outcome": [],
    "Manhattan_Trajectory_length": [],
    "Manhattan_Actual_length": [],
}

p0 = 36
for i in range(1,p0, 4):
    for j in range(10):
        print(i, j)
        grid_len = 101
        result["Dimension"].append(grid_len)
        result["Probability"].append(i/100)
        matrix = create_grid(grid_len, i/100)
        # result["Matrix"].append(matrix)

        # knowledge = matrix
        knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]
        # print_grid(matrix)
        # print_grid(knowledge)
        start = Node()
        start.position = (0, 0)
        goal = Node()
        goal.position = (grid_len-1, grid_len-1)
        no_of_blocks = count_blocks(matrix)
        result["No_of_blocks"].append(no_of_blocks)
        density = no_of_blocks/(grid_len**2)
        result["Density"].append(density)

        # print_grid(matrix)
        #MANHATTAN METRICS
        cost = 1
        res = repeated(matrix, knowledge, start, goal, cost)
        # print(res)
        outcome = 0
        if res[0] != None:
            outcome = 1
            path = Astar(matrix, start, goal)
            result["Manhattan_Actual_length"].append(len(path))
            result["Manhattan_Trajectory_length"].append(res[1])
        else:
            result["Manhattan_Actual_length"].append(None)
            result["Manhattan_Trajectory_length"].append(None)
        
        result["Manhattan_outcome"].append(outcome)

        

data = pd.DataFrame(result)
data.to_csv("Question6.csv", index=False, encoding='utf-8')