from Utils import create_grid, print_grid, count_blocks
from Node import Node
from RepeatedAStar import Astar
import pandas as pd
from time import time

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

def repeated(matrix, knowledge, start, end, cost, heuristic="manhattan"):
    flag = False
    while True:
        res = Astar(knowledge, start, end, heuristic)
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
    "Dimension":[],
    "Probability": [],
    "No_of_blocks":[],
    "Density": [],
    "Cells_Processed": [],
    "Shortest_Path_In_Final_Discovered_Grid": [],
    "Shortest_Path_In_Full_Grid": [],
    "Outcome": [],
    "Trajectory_length": [],
    "Time_taken": []
}

p0 = 26
for i in range(1,p0, 4):
    for j in range(100):
        print(i, j, "iteration")
        grid_len = 101
        result["Dimension"].append(grid_len)
        result["Probability"].append(i/100)
        matrix = create_grid(grid_len, i/100)

        knowledge = [ [ "-" for i in range(grid_len) ] for j in range(grid_len) ]
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
        begin = time()
        res = repeated(matrix, knowledge, start, goal, cost)
        end = time() - begin
        # print(res)
        # print_grid(knowledge)
        outcome = 0
        if res[0] != None:
            outcome = 1
            cost_2 = 0
            res_rep = Astar(knowledge, start, goal, False)
            path = Astar(matrix, start, goal)
            if path[0] != None:
                result["Shortest_Path_In_Final_Discovered_Grid"].append(len(res_rep[0]))
                result["Shortest_Path_In_Full_Grid"].append(len(path[0]))
                result["Trajectory_length"].append(res[1])
            else:
                result["Shortest_Path_In_Final_Discovered_Grid"].append(None)
                result["Shortest_Path_In_Full_Grid"].append(None)
                result["Trajectory_length"].append(None)

        else:
            result["Shortest_Path_In_Final_Discovered_Grid"].append(None)
            result["Shortest_Path_In_Full_Grid"].append(None)
            result["Trajectory_length"].append(None)

        cells_not_covered  = 0
        for k in range(len(knowledge)):
            for l in range(len(knowledge[0])):
                if k == 0 and l == 0:
                    continue
                if knowledge[k][l] == '-':
                    cells_not_covered+=1
        
        result["Cells_Processed"].append(grid_len**2-cells_not_covered)
        result["Time_taken"].append(end)
        result["Outcome"].append(outcome)

print(result)
data = pd.DataFrame(result)
data.to_csv("Question6-total-final.csv", index=False, encoding='utf-8')