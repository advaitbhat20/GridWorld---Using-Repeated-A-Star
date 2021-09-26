from Utils import create_grid, print_grid, count_blocks
from Node import Node
from Astar import Astar
from Exceution import repeated       

grid_len = 5
matrix = create_grid(grid_len, 0.75)
print_grid(matrix)

knowledge = [ [ 0 for i in range(grid_len) ] for j in range(grid_len) ]

print("")
print_grid(knowledge)
print("")

start = Node()
start.position = (0, 0)
goal = Node()
goal.position = (grid_len-1, grid_len-1)

print("Repeated Astar unknown world", repeated(matrix, knowledge, start, goal))

print("##############")
print("Repeated Astar known world", repeated(matrix, matrix, start, goal))
print("Final update knowledge")
print_grid(knowledge)

#Final output
print("Final Path", Astar(knowledge, start, goal))