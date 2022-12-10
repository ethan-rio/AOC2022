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
total = 0
def draw(t, x):
    t1 = t-1
    grid[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
    if t in nth_cycle:
        total += x*t



for l in lines:
    params = l.split(" ")
    cmd = params[0]
    if len(params) > 1:
        reg_temp = int(params[1]) 
    # print("Cur X: ", X, " ----- Input: ",reg_temp)
    if cmd == 'noop':
        cycle += 1
        arrays.append(X)
        print(cycle, ": ", X)
    if cmd == 'addx':
        for i in range(2):
            cycle += 1
            if i == 1:
                X += reg_temp
            print(cycle, ": ", X)
            arrays.append(X)
print(arrays)

total = 0
for i in nth_cycle:
    total += arrays[i-1] * i
    

print(total)

            

for r in range(6):
    print(''.join(grid[r]))