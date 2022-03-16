with open("input", "r") as f:
    heightmap = []
    for line in f:
        row = []
        for n in line.strip():
            row.append(int(n))
        heightmap.append(row)

def find_local_minimum_coords(M):
    local_minimum_coords = []

    rows, columns = len(M), len(M[0])
    # corners
    # top-left
    if M[0][0] < M[0][1] and M[0][0] < M[1][0]:
        local_minimum_coords.append((0, 0))
      
    # top-right
    if M[0][-1] < M[0][-2] and M[0][-1] < M[1][-1]:
        local_minimum_coords.append((0, columns-1))
      
    # bottom-right
    if M[-1][-1] < M[-1][-2] and M[-1][-1] < M[-2][-1]:
        local_minimum_coords.append((rows-1, columns-1))
      
    # bottom-left
    if M[-1][0] < M[-1][1] and M[1][0] < M[-2][0]:
        local_minimum_coords.append((rows-1, 0))
      
    # top edge
    for j in range(1, columns-1):   
        if M[0][j] < M[0][j-1] and M[0][j] < M[1][j] and M[0][j] < M[0][j+1]:
            local_minimum_coords.append((0, j))

    # right edge
    for i in range(1, rows-1):
        if M[i][-1] < M[i-1][-1] and M[i][-1] < M[i][-2] and M[i][-1] < M[i+1][-1]:
            local_minimum_coords.append((i, columns-1))

    # bottom edge
    for j in range(1, columns-1):
        if M[-1][j] < M[-1][j-1] and M[-1][j] < M[-2][j] and M[-1][j] < M[-1][j+1]:
            local_minimum_coords.append((rows-1, j))
    
    # left edge
    for i in range(1, rows-1):
        if M[i][0] < M[i-1][0] and M[i][0] < M[i][1] and M[i][0] < M[i+1][0]:
            local_minimum_coords.append((i, 0))

    # any others    
    for i in range(1, rows-1):
        for j in range(1, columns-1):
            if M[i][j] < M[i][j + 1] and M[i][j] < M[i][j - 1] and M[i][j] < M[i + 1][j] and M[i][j] < M[i - 1][j]:
                local_minimum_coords.append((i, j))

    return local_minimum_coords

low_points = find_local_minimum_coords(heightmap)
solution = sum([heightmap[i][j]+1 for i,j in low_points])
print(f"The solution of part 1 is: {solution}")

# part 2
def get_neighboors(point, M):
    rows, columns = len(M), len(M[0])
    i,j = point

    # case corners
    # top-left
    if i == j == 0:
        return [(0, 1), (1, 0)]
    # top-right
    if i == 0 and j == columns-1:
        return [(0, j-1), (1, j)]
    # bottom-right
    if i == rows-1 and j == columns-1:
        return [(i, j-1), (i-1, j)]
    # bottome-left
    if i == rows and j == 1:
        return [(i-1, j), (i, j+1)]

    # case edges
    # top
    if i == 0:
        return [(0, j-1), (1, j), (0, j+1)]
    # right
    if j == columns-1:
        return [(i-1, j), (i, j-1), (i+1, j)]
    # bottom
    if i == rows-1:
        return [(i, j-1), (i-1, j), (i, j+1)]
    # left
    if j == 0:
        return [(i-1, 0), (i, 1), (i+1, 0)]

    # otherwise
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def expand_basian(low_point, M):
    basian = set([low_point])
    queue = [low_point]
    while len(queue) != 0: 
        x = queue.pop()
        if M[x[0]][x[1]] != 9:
            basian.add(x)
            neighs = get_neighboors(x, M)
            for y in neighs:
                if y not in basian:
                    queue.insert(0, y)
    return basian

basians_sizes = [len(expand_basian(x, heightmap)) for x in low_points]
from math import prod
solution = prod(sorted(basians_sizes, reverse=True)[:3])
print(f"The solution of part 2 is: {solution}")

import matplotlib.pyplot as plt
plt.imshow(heightmap, cmap='hot')
plt.show()
