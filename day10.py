from collections import defaultdict
import numpy as np
with open("day10.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# print(len(lines))

nth_cycle = [20, 60, 100, 140, 180, 220]
arrays = [1]
X = 1
cycle = 0
grid = [['X' for _ in range(40)] for _ in range(6)]
def draw(cycle, x):
    i = cycle-1
    global grid
    row = i // 40
    col = i % 40
    if abs(x-(i%40))<=1:
        grid[row][col] = 'E'
    else:
        grid[row][col] = ' '


for l in lines:
    params = l.split(" ")
    cmd = params[0]
    if len(params) > 1:
        reg_temp = int(params[1]) 
    if cmd == 'noop':
        cycle += 1
        arrays.append(X)
        draw(cycle, X)
    if cmd == 'addx':
        for i in range(2):
            cycle += 1
            draw(cycle, X)
            if i == 1:
                X += reg_temp
            arrays.append(X)
print(arrays)

total = 0
for i in nth_cycle:
    total += arrays[i-1] * i
    

print(total)

for i in range(6):
    print(''.join(grid[i]))

            

