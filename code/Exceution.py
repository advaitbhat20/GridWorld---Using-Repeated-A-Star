from Astar import Astar
from Utils import print_grid
from Node import Node

def implement(matrix, knowledge, path):
  for itr in  range(1,len(path)):
    i = path[itr][0]
    j = path[itr][1]
    print("(i,j) -- ", i, j)
    if matrix[i][j] == 1:
      print("ended node", path[itr-1])  
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

def repeated(matrix, knowledge, start, end):
    flag = False
    #Update knowledge for the first time from the start position
    # i = j = 0
    # if i+1 < len(matrix) and matrix[i+1][j] == 1:
    #   knowledge[i+1][j] = 1
    # if j+1 < len(matrix[0]) and matrix[i][j+1] == 1:
    #   knowledge[i][j+1] = 1
    while True:
        print("################")
        print_grid(knowledge)
        path = Astar(knowledge, start, end)
        print(path)

        if path:
            last = implement(matrix, knowledge, path)
            last_Node = Node(last)
            print("lastNode", last_Node)
            # if path[0] == last:
            #     print("error?")
            #     break
            if path[len(path)-1] == last:
                print("Agent goal!!")
                flag = True
                break
            start = last_Node

        else:
            print("no path planned it got stuck")
            break

    return path