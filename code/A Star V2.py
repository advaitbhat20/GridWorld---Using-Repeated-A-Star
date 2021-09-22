# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import pandas as pd
import random
import threading
import math
import collections
import heapq
import warnings
from queue import Queue
from time import monotonic as time
try:
    from _queue import Empty
except ImportError:
    class Empty(Exception):
        'Exception raised by Queue.get(block=0)/get_nowait().'
        pass
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

    def __hash__(self):
       
        # hash(custom_object)
        return hash((self.position, self.parent))
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
    
    def get_neigbours(self):   
        #This returns the neighbours of the Node
        neighbour_cord = [(-1, 0),(0, -1),(0, 1),(1, 0)]
        current_x = self.position[0]
        current_y = self.position[1]
        neighbours = []
        for n in neighbour_cord:
            x = current_x + n[0]
            y = current_y + n[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix):
                c = Node()
                c.position = (x, y)
                c.parent = Node
                neighbours.append(c)
        return neighbours
    

class PriorityQueue:
  
  def __init__(self):
    self.queue = list()
    self.mutex = threading.Lock()
    self.not_empty = threading.Condition(self.mutex)

    # Notify not_full whenever an item is removed from the queue;
    # a thread waiting to put is notified then.
    self.not_full = threading.Condition(self.mutex)

    # Notify all_tasks_done whenever the number of unfinished tasks
    # drops to zero; thread waiting to join() is notified to resume
    self.all_tasks_done = threading.Condition(self.mutex)
    self.unfinished_tasks = 0
    
    
  def insert(self, node,priority):
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
  
  def get(self):
    # remove the first node from the queue
    return self.queue.pop(0)

  
    
  def show(self):
    for x in self.queue:
      print (str(x.position)+" - "+str(x.f))
  
  def size(self):
    return len(self.queue)

  def empty(self):
      with self.mutex:
            return not self.size()
        


class grid_voyage:
    
    def __init__(self):
        self.data = list()
    
    
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
    # Initialize a priority queue
    Initial = PriorityQueue()
    Initial.insert(start,0)
    
    cost_now = {start: 0}
    came_from = {start: None}
    
    while not Initial.empty():
        current = Initial.get()
        if current == end:
            break
        for n in current.get_neigbours():
            Cost_Counter= cost_now[current]+knowledge_grid.cost(current,n)
            if n not in cost_now or Cost_Counter < cost_now[n]:
                cost_now[n] = Cost_Counter
                priority = Cost_Counter + calc_manhattan(end, n)
                Initial.insert(n, priority)
                came_from[n] = current
    path = []
    while current.parent is not None:
        path.append(current.position)
        current = current.parent
    path.append(current.position)
    return path[::-1]

    return 0

######################################################
# Function calls after this
knowledge_grid=grid_voyage()
matrix = grid_voyage.create_grid(5)
grid_voyage.print_grid(matrix)

knowledge = [ [ 0 for i in range(5) ] for j in range(5) ]

start = Node()
start.position = (0, 0)
goal = Node()
goal.position = (4, 4)
s = astar(knowledge_grid, start, goal)
print(s)
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