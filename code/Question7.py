from Utils import create_grid, print_grid, count_blocks
from Node import Node
from RepeatedAStar import Astar
import pandas as pd
from time import time

def implement(matrix, knowledge, path):
    for itr in  range(1,len(path)):
        i = path[itr][0]
        j = path[itr][1]
        # print("(i,j) -- ", i, j)
        # print("Check here",matrix[i][j])
        if matrix[i][j] == 1:
            knowledge[i][j] = 1
            return path[itr-1]
        else:
            knowledge[i][j] = 0
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
        # print("Path ASTAR",path)
        if path:
            last = implement(matrix, knowledge, path)
            # print(last, len(path), path.index(last), cost)
            cost = cost + path.index(last)

            last_Node = Node(last)
            # print(last_Node.position)
            # print("lastNode", last_Node, path[len(path)-1] == last)
            if path[len(path)-1] == last:
                # print("Agent goal!!")
                flag = True
                break
            # print("if Skipped")
            start = last_Node
            # print("start", start, flag)
            # print("neightbours", start.get_neigbours(matrix))


        else:
            # print("no path planned it got stuck")
            break
    return (path,cost)



result = {
    "Dimension":[],
    "Probability": [],
    "No_of_blocks":[],
    "Density": [],
    "Total_Cells_Discovered": [],
    "Total_Blocked_Cells_Discovered": [],
    "Manhattan_outcome": [],
    "Manhattan_Trajectory_length": [],
    "Manhattan_Actual_length": [],
    "Time_taken": []
}

p0 = 36
for i in range(1,p0, 4):
    for j in range(50):
        # print(i, j, "iteration")
        grid_len = 101
        result["Dimension"].append(grid_len)
        result["Probability"].append(i/100)
        matrix = create_grid(grid_len, i/100)
        # result["Matrix"].append(matrix)

        # knowledge = matrix
        knowledge = [ [ "-" for i in range(grid_len) ] for j in range(grid_len) ]
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

        #print_grid(matrix)
        #MANHATTAN METRICS
        cost = 1
        begin = time()
        res = repeated(matrix, knowledge, start, goal, cost)
        end = time() - begin
        # print(res)
        #print_grid(knowledge)
        outcome = 0
        if res[0] != None:
            outcome = 1
            path = Astar(matrix, start, goal)
            if path[0] != None:
                # print(path[0], len(path[0]), type(path[0]), "path")
                result["Manhattan_Actual_length"].append(len(path[0]))
                result["Manhattan_Trajectory_length"].append(res[1])
            else:
                result["Manhattan_Actual_length"].append(None)
                result["Manhattan_Trajectory_length"].append(None)

        else:
            result["Manhattan_Actual_length"].append(None)
            result["Manhattan_Trajectory_length"].append(None)

        cells_not_covered  = 0
        cells_knowledge = 0
        for k in range(len(knowledge)):
            for l in range(len(knowledge[0])):
                if k == 0 and l == 0:
                    continue
                if knowledge[k][l] == '-':
                    cells_not_covered+=1
                if knowledge[k][l] == 1:
                    cells_knowledge += 1
        
        # print("Hello", grid_len**2-cells_not_covered)
        # print("Bhag", cells_knowledge)
        # print_grid(knowledge)
        result["Total_Blocked_Cells_Discovered"].append(cells_knowledge)
        result["Total_Cells_Discovered"].append(grid_len**2-cells_not_covered)
        result["Time_taken"].append(end)
        result["Manhattan_outcome"].append(outcome)

# print(result)
data = pd.DataFrame(result)
data.to_csv("Question6_2-total-final.csv", index=False, encoding='utf-8')