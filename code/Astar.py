from queue import PriorityQueue
from dataclasses import dataclass, field
from Utils import calc_manhattan, calc_euclidean, calc_chebyshev

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
        print(counter, len(pQueue.queue))
        if counter > 20000:
            print(knowledge_grid)
            return None

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
            return path[::-1]

        for n in current.get_neigbours(knowledge_grid):
            #check if neighbor is in closed set
            if n.position in closed_hash:
                continue

            #calculate heuristics for the neighbor
            n.g = current.g + 1
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

    return None
