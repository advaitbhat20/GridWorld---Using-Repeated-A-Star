from Utils import create_grid, print_grid, count_blocks, calc_manhattan, calc_euclidean, calc_chebyshev
from Node import Node
from queue import PriorityQueue
from dataclasses import dataclass, field
from time import time

@dataclass(order=True)
class PrioritizedItem:
    priority: float
    item: object = field()

def Astar(knowledge_grid, start, end, heuristic="manhattan"):
    grid_len = len(knowledge_grid)
    # Initialize a priority queue
    
    pQueue = PriorityQueue()
    pQueue.put(PrioritizedItem(0.0, start))
    closed_hash = {}    

    counter = 0
    
    while not pQueue.empty():
        # print(counter, len(pQueue.queue))
        if counter > 20000:
            print(knowledge_grid)
            return [None, len(closed_hash)]

        counter+=1

        current = pQueue.get().item
        # print("current", current)

        #Using dictionary instead of a list, to make retrival easier
        closed_hash[current.position] = True

        # print("closed hash", closed_hash)

        # Check if we have reached the goal, return the path
        if current == end:
            # print("Astar goal!")
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
            n.f = n.g + n.h
            #check if node is in priority queue if yes does it have lower value?

            #add n to priority queue
            (x, y) = n.position
            if knowledge_grid[x][y] != 1:
                # print("add to queue", n)
                # print(n.f, n.position, heuristic)
                pQueue.put(PrioritizedItem(float(n.f), n))

    return [None]

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
    aCost = 0
    while True:
        

        res = Astar(knowledge, start, end, heuristic)
        path = res[0]
        aCost += res[1]
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
    return (path,cost,aCost)


if __name__ == "__main__":
    grid_len = 101
    matrix = create_grid(grid_len, 0.13)
    # print_grid(matrix)

    knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]

    # print("")
    # print_grid(knowledge)
    # print("")

    start = Node()
    start.position = (0, 0)
    goal = Node()
    goal.position = (grid_len-1, grid_len-1)

    cost = 0
    begin = time()
    print("Repeated Astar unknown world Manhattan", repeated(matrix, knowledge, start, goal, cost))

    # print(time()-begin)
    # print("Repeated Astar unknown world Euclidean", repeated(matrix, knowledge, start, goal, "euclidean"))
    # print("Repeated Astar unknown world Chebyshev", repeated(matrix, knowledge, start, goal, "chebyshev"))

    # print("##############")
    # # print("Repeated Astar known world", repeated(matrix, matrix, start, goal))
    # print("Final update knowledge")
    # print_grid(knowledge)

    #Final output
    # print("Final Path", Astar(knowledge, start, goal))