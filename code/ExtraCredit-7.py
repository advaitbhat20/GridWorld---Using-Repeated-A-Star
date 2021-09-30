from Utils import create_grid, print_grid, count_blocks
from collections import deque
from time import time
import pandas as pd

class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, dist: int, parent: Point):
        self.pt = pt # The coordinates of the cell
        self.dist = dist # Cell's distance from the source
        self.parent = parent

def isValid(row: int, col: int):
    return (row >= 0) and (row < grid_len) and (col >= 0) and (col < grid_len)

def queueQQ(curr):
    while curr != None:
        print(curr.pt.x, curr.pt.y, end=":;")
        curr = curr.parent
    print("")

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point):
    visited = [[False for i in range(len(mat))]
                       for j in range(len(mat[0]))]
    
    # Mark the source cell as visited
    visited[src.x][src.y] = True
     
    # Create a queue for BFS
    q = deque()
     
    # Distance of source cell is 0
    s = queueNode(src,0, None)
    q.append(s) #  Enqueue source cell
     
    # Do a BFS starting from source cell
    while q:
 
        curr = q.popleft() # Dequeue the front cell
         
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            # queueQQ(curr)
            
            path = []
            while curr.parent!=None:
                # print(curr.pt.x, curr.pt.y, "before")
                path.append((curr.pt.x, curr.pt.y))
                curr = curr.parent
                # print(curr.pt.x, curr.pt.y, "after")
            path.append((src.x, src.y))
            # print_grid(visited)
            return [path[::-1], visited]
         
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            # if adjacent cell is valid, has path 
            # and not visited yet, enqueue it.
            if (isValid(row,col) and
               mat[row][col] == 0 and
                not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1, curr)
                q.append(Adjcell)
     
    # Return -1 if destination cannot be reached
    return [None, visited]

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
    return path[len(path)-1]

def repeated(matrix, knowledge, start, end, cost):
    flag = False
    while True:
        res = BFS(knowledge, start, end)
        # print(res, "result")
        path = res[0]
        # print("Path ASTAR",path)
        if path:
            last = implement(matrix, knowledge, path)
            # print(last, len(path), path.index(last), cost)
            cost = cost + path.index(last)
            # print(last, "last")
            last_Node = Point(last[0], last[1])
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
    return (path,cost, res[1])


# This code is contributed by stutipathak31jan
result = {
    "Dimension":[],
    "Probability": [],
    "No_of_blocks":[],
    "Density": [],
    "Cells_Processed": [],
    "Shortest_Path_In_Final_Discovered_Grid": [],
    "Shortest_Path_In_Full_Grid": [],
    "Trajectory_length": [],
    "Outcome": [],
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
        # result["Matrix"].append(matrix)

        # knowledge = matrix
        knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]
        # print_grid(matrix)
        # print_grid(knowledge)
        start = Point(0,0)
        goal = Point(grid_len-1, grid_len-1)
        no_of_blocks = count_blocks(matrix)
        result["No_of_blocks"].append(no_of_blocks)
        density = no_of_blocks/(grid_len**2)
        result["Density"].append(density)

        # print_grid(matrix)
        #BFS METRICS
        cost = 1
        begin = time()
        # print(BFS(matrix, start, goal), "BFS")
        res = repeated(matrix, knowledge, start, goal, cost)
        updated_knowledge = res[2]
        end = time() - begin
        # print(res)
        # print_grid(knowledge)
        outcome = 0
        if res[0] != None:
            outcome = 1
            cost_2 = 0
            res_rep = BFS(knowledge, start, goal)
            path = BFS(matrix, start, goal)
            # print(path, "AWOWO")
            if path != None:
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
        for k in range(len(updated_knowledge)):
            for l in range(len(updated_knowledge[0])):
                if updated_knowledge[k][l] == False:
                    cells_not_covered+=1
        
        result["Cells_Processed"].append(grid_len**2-cells_not_covered)
        result["Time_taken"].append(end)
        result["Outcome"].append(outcome)

print(result)
data = pd.DataFrame(result)
data.to_csv("ExtraQuestion7-total-final.csv", index=False, encoding='utf-8')