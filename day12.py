from collections import defaultdict, deque
import numpy as np
with open("day12.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
row = len(lines)
col = len(lines[0])


print("Row, col: ", row, col)
grid = [[0 for _ in range(col)] for _ in range(len(lines))]
for i in range(row):
    line = lines[i]
    for j in range(col):
        c = lines[i][j]
        if c == "S":
            grid[i][j] = 1
            print("S: ", i, j)
        elif c == "E":
            grid[i][j] = 27
            print("E: ", i, j)
        else:
            grid[i][j] = ord(c)-ord('a')+1
        # print(c, grid[i][j])

def BFS(Q):
    S = set()
    while Q:
        (i,j),dis = Q.popleft()
        if lines[i][j]=='E':
            return dis
        if (i,j) in S: # visited vertex
            continue
        S.add((i,j))
        for delta_i,delta_j in [(0,1),(1,0),(0,-1),(-1,0)]:
            di = i + delta_i
            dj = j + delta_j
            if 0<=di<row and 0<=dj<col and (grid[di][dj] - grid[i][j]) <= 1:
                Q.append(((di,dj), dis + 1))

# PART 1
Q = deque()
for i in range(row):
    for j in range(col):
        if lines[i][j]=='S':
            Q.append(((i,j), 0))
print("Part 1: ", BFS(Q))

# Part 2
Q = deque()
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1:
            Q.append(((i,j), 0))
print("Part 2: ", BFS(Q))
