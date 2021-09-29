from Utils import create_grid, print_grid, count_blocks
from Node import Node
from RepeatedAStar import Astar
from RepeatedAStar import repeated
import pandas as pd

result = {
    "Dimension":[],
    "Probability": [],
    "No_of_blocks":[],
    "Density": [],
    "Outcome": [],
    "Length_of_path": []
}
for i in range(1, 100, 1):
    for j in range(20):
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
        cost = 0
        res = repeated(matrix, knowledge, start, goal, cost)
        outcome = 0
        if res[0] != None:
            outcome = 1
            res_1 = Astar(knowledge, start, goal, "manhattan")

            path = len(res_1[0])
            result["Length_of_path"].append(path)

        else:
            path = None
            result["Length_of_path"].append(None)

        result["Outcome"].append(outcome)

data = pd.DataFrame(result)
data.to_csv("Data1.csv", index=False, encoding='utf-8')