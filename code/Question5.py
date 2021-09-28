from Utils import create_grid, print_grid, count_blocks
from Node import Node
from Astar import Astar
from Exceution import repeated
import pandas as pd
from time import time

result = {
    "Dimension":[],
    "Probability": [],
    "No_of_blocks":[],
    "Density": [],
    "Manhattan_outcome": [],
    "Manhattan_length_of_path": [],
    "Manhattan_time": [],
    "Euclidean_outcome": [],
    "Euclidean_length_of_path": [],
    "Euclidean_time": [],
    "Chebyshev_outcome": [],
    "Chebyshev_length_of_path": [],
    "Chebyshev_time": [],

}
for j in range(50):
    p0 = 0.31
    grid_len = 20
    result["Dimension"].append(grid_len)
    result["Probability"].append(p0)
    matrix = create_grid(grid_len, p0)
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
    #MANHATTAN METRICS
    start_time = time()
    res = repeated(matrix, knowledge, start, goal)
    end = time() - start_time
    result["Manhattan_time"] = end
    outcome = 0
    if res != None:
        outcome = 1
        path = len(Astar(matrix, start, goal))
    else:
        path = None
    result["Manhattan_outcome"].append(outcome)
    result["Manhattan_length_of_path"].append(path)

    #EUCLIDEAN METRICS
    start_time = time()
    res = repeated(matrix, knowledge, start, goal, "euclidean")
    end = time() - start_time
    result["Euclidean_time"] = end
    outcome = 0
    if res != None:
        outcome = 1
        path = len(Astar(matrix, start, goal, "euclidean"))
    else:
        path = None
    result["Euclidean_outcome"].append(outcome)
    result["Euclidean_length_of_path"].append(path)

    #CHEBYSHEV METRICS
    start_time = time()
    res = repeated(matrix, knowledge, start, goal, "chebyshev")
    end = time() - start_time
    result["Chebyshev_time"] = end
    outcome = 0
    if res != None:
        outcome = 1
        path = len(Astar(matrix, start, goal, "chebyshev"))
    else:
        path = None
    result["Chebyshev_outcome"].append(outcome)
    result["Chebyshev_length_of_path"].append(path)


data = pd.DataFrame(result)
data.to_csv("Comparision.csv", index=False, encoding='utf-8')