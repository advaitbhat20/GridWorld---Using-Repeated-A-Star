import numpy as np
# import pandas as pd
import random
import math

class Node:
    # Initialize the class
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

class PriorityQueue:
  
  def __init__(self):
    self.queue = list()
    
  def insert(self, node):
    # if queue is empty
    if self.size() == 0:
      # add the new node
      self.queue.append(node)
    else:
      # traverse the queue to find the right place for new node
      for x in range(0, self.size()):
        # if the heuristic of new node is less than
        if node.f >= self.queue[x].f:
          # if we have traversed the complete queue
          if x == (self.size()-1):
            # add new node at the end
            self.queue.insert(x+1, node)
          else:
            continue
        else:
          self.queue.insert(x, node)
          return True
  
  def delete(self):
    # remove the first node from the queue
    return self.queue.pop(0)
    
  def show(self):
    for x in self.queue:
      print (str(x.position)+" - "+str(x.f))
  
  def size(self):
    return len(self.queue)

def create_grid(n):
    matrix = [ [ 0 for i in range(n) ] for j in range(n) ]

    p = 0.75
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0) or (i==n-1 and j==n-1):
                matrix[i][j] = 0
            else:
                prob = random.uniform(0, 1)
                if prob >= p:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
    return matrix

def print_grid(matrix):
    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")

def calc_manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def calc_euclidean(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def calc_chebyshev(a,b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def astar(knowledge_grid,start,end):
    # Initialize open and closed list
    open_list = []
    closed_list = []

    return 0

######################################################
# Function calls after this

matrix = create_grid(5)
print_grid(matrix)

knowledge = [ [ 0 for i in range(5) ] for j in range(5) ]


pQueue = PriorityQueue()
node1 = Node([0,0],)
node2 = Node([2,2],[1,2])
node3 = Node([1,3],[1,2])

node1.f = calc_manhattan(node1.position, [5,5])
node2.f = calc_manhattan(node2.position, [5,5])
node3.f = calc_manhattan(node3.position, [5,5])


pQueue.insert(node1)
pQueue.insert(node2)
pQueue.insert(node3)

pQueue.show()
