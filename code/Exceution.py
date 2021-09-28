from Astar import Astar
from Utils import print_grid
from Node import Node

def implement(matrix, knowledge, path):
    for itr in  range(1,len(path)):
        i = path[itr][0]
        j = path[itr][1]
        # print("(i,j) -- ", i, j)
        # print("Check here",matrix[i][j])
        if matrix[i][j] == 1:
            knowledge[i][j] = 1 
            return path[itr-1]
        if i+1<len(matrix) and matrix[i+1][j]==1:
            knowledge[i+1][j] = 1
        if j+1<len(matrix) and matrix[i][j+1]==1:
            knowledge[i][j+1] = 1
        if i-1>0 and matrix[i-1][j]==1:
            knowledge[i-1][j] = 1
        if j-1>0 and matrix[i][j-1]==1:
            knowledge[i][j-1] = 1
    return path[len(path)-1]

def repeated(matrix, knowledge, start, end, cost, heuristic="manhattan"):
    flag = False
    while True:
        # print("################")
        # print_grid(knowledge)
        path = Astar(knowledge, start, end, heuristic)
        # print("Path ASTAR",path)
        if path:
            last = implement(matrix, knowledge, path)
            # print(last, len(path), path.index(last), cost)
            cost = cost + path.index(last)
            last_Node = Node(last)
            # print("lastNode", last_Node, path[len(path)-1] == last)
            if path[len(path)-1] == last:
                # print("Agent goal!!")
                flag = True
                break
            # print("if Skipped")
            start = last_Node
            print("start", start, flag)
            print("neightbours", start.get_neigbours(matrix))


        else:
            # print("no path planned it got stuck")
            break
    return (path,cost)