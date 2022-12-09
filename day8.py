from collections import defaultdict
import numpy as np
with open("day8.txt", "r") as f:
    lines = f.read().strip().split()

trees_grid = [list(map(int, list(l))) for l in lines]

n = len(trees_grid)
m = len(trees_grid[0])

trees_grid = np.array(trees_grid)

total = 0

for i in range(n):
    for j in range(m):
        h = trees_grid[i,j]
        if j == 0 or np.amax(trees_grid[i, :j]) < h:
            total += 1
        elif i == 0 or np.amax(trees_grid[:i, j]) < h:
            total += 1
        elif j == m - 1 or np.amax(trees_grid[i, (j+1): ]) < h:
            total += 1
        elif i == n -1 or np.amax(trees_grid[(i+1):, j]) < h:
            total += 1
    
print(total)

total = 0
neighbours = [[0,1], [0, -1], [1,0], [-1, 0]]

for i in range(n):
    for j in range(m):
        h = trees_grid[i, j]
        point = 1
        for x, y in neighbours:
            z, t = i, j
            dist = 0
            z += x
            t += y
            print("du ma du ma")
            while( 0 <= z < n and 0 <= t < m) and trees_grid[z, t] < h:
                dist += 1
                z += x
                t += y
                print(dist, z, t)
                if (0 <= z < n and 0 <= t < m) and trees_grid[z, t] >= h:
                    dist += 1
            
            point *= dist
        total = max(total, point)

print(total)