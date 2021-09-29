from Utils import create_grid, print_grid


def explore_neighbors(r, c):
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        
        if rr < 0 or cc < 0:
            continue
        if rr >= grid_len or cc >= grid_len:
            continue
        
        if visited[r][c] == True:
            continue
        if m[r][c] == '1':
            continue
        
        rq.put(rr)
        rc.put(cc)
        visited[r][c] = True
        
        nodes_in_next_layer += 1

def bfs():
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    global nodes_left_in_layer
    global reached_end
    
    print(rq, "rq")
    while len(rq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)
        if (r,c) == (grid_len-1, grid_len-1):
            reached_end = True
            break
        explore_neighbors(r, c)
        
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end == True:
        return move_count
    return -1

grid_len = 5
matrix = create_grid(grid_len, 33/100)
print_grid(matrix)

sr,sc = 0,0
rq = []
cq = []

move_count = 0
nodes_left_in_layer = 0
nodes_in_next_layer = 1

reached_end = False
# Matrix to keep track of visited cells.
visited = [[0 for i in range(grid_len) ] for j in range(grid_len)]
# North, South, East and West direction vectors
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

print(bfs())
print_grid(visited)
