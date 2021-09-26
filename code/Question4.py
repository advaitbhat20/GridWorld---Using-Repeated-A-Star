from Utils import create_grid, print_grid, count_blocks
from Node import Node
from Astar import Astar
from Exceution import repeated
import pandas as pd

result = {
    "Dimension":[],
    "Probability": [],
    "No_of_blocks":[],
    "Density": [],
    "Outcome": [],
    "Length_of_path": []

}
for i in range(1,100):
    for j in range(100):
        grid_len = 101
        result["Dimension"].append(grid_len)
        result["Probability"].append(i/100)
        matrix = create_grid(grid_len, i/100)
        knowledge = matrix
        start = Node()
        start.position = (0, 0)
        goal = Node()
        goal.position = (grid_len-1, grid_len-1)
        no_of_blocks = count_blocks(matrix)
        result["No_of_blocks"].append(no_of_blocks)
        density = no_of_blocks/(grid_len**2)
        result["Density"].append(density)

        # print_grid(matrix)
        res = repeated(matrix, knowledge, start, goal)
        outcome = 0
        if res != None:
            outcome = 1
            path = len(Astar(matrix, start, goal))
        else:
            path = None
        result["Outcome"].append(outcome)
        result["Length_of_path"].append(path)

data = pd.DataFrame(result)
data.to_csv("Data.csv", index=False, encoding='utf-8')