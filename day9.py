from collections import defaultdict
import numpy as np
with open("day9.txt", "r") as f:
    moves = [l.strip() for l in f.readlines()]

def vector(h_pos, t_pos):
    return [h_pos[0]-t_pos[0], h_pos[1]-t_pos[1]]

def safe_pos(t_pos):
    safe_pos = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            safe_pos.append([t_pos[0] + i, t_pos[1] + j])

    return safe_pos

def move_single(h_pos, t_pos, move):
    new_h_pos = h_pos.copy()
    new_t_pos = t_pos.copy()
    safe_positions = safe_pos(t_pos)
    
    if move == 'U':
        new_h_pos[1] = h_pos[1] + 1
    if move == 'D':
        new_h_pos[1] = h_pos[1] - 1
    if move == 'L':
        new_h_pos[0] = h_pos[0] - 1
    if move == 'R':
        new_h_pos[0] = h_pos[0] + 1
    # print("Vector: ", vector(new_h_pos, t_pos))

    if new_h_pos in safe_positions:
        return new_h_pos, new_t_pos
    else:
        new_t_pos = h_pos
    return new_h_pos, new_t_pos

# Part 1

h = [0,0]
t = [0,0]
t_trails_1 = [[0,0]]
t_trails_2 = [[0,0]]
for move in moves:
    direction, count = move.split(" ")
    count = int(count)
    for i in range(count):
        h, t = move_single(h, t, direction)
        t_trails_1.append(t)

unique_list = []
for i in t_trails_1:
    if i not in unique_list:
        unique_list.append(i)

# print(unique_list)
print(len(unique_list))

# Part 2

h = [0,0]
t = [[0,0] for _ in range(9)]
t_trails_2 = [[0,0]]
for move in moves:
    direction, count = move.split(" ")
    count = int(count)
    for i in range(count):
        h, t[0] = move_single(h, t[0], direction)
        for i in range(1, 9):
            t[i] = move_single(t[i-1], t[i], direction)
        t_trails_2.append(t[8])

unique_list = []
for i in t_trails_2:
    if i not in unique_list:
        unique_list.append(i)

# print(unique_list)
print(len(unique_list))


