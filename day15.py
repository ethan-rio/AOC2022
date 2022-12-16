from collections import defaultdict
import numpy as np
with open("day15.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# print(len(lines))
sensors = []
beacons = []

def dis(p1, p2): #p1: sensor
    dis = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    # x_min, x_max, y_min, y_max
    return dis

def is_valid(x, y, distance):
    if x + y > distance:
        return False
    return True

def count_set(point, distance): # This is a dead-end
    res = set()
    px = point[0]
    py = point[1]
    arrays = []
    for x in range(distance+1):
        for y in range(distance+1):
            if not is_valid(x, y, distance):
                continue
            else:
                res.add((px + x, py + y))
    return res

arrays = []
for l in lines:
    temp = l.split(" ")
    Sx = int(temp[2].split("=")[1].split(",")[0])
    Sy = int(temp[3].split("=")[1].split(":")[0])
    Bx = int(temp[-2].split("=")[1].split(",")[0])
    By = int(temp[-1].split("=")[1].split(":")[0])
    sensors.append((Sx, Sy))
    beacons.append((Bx, By))
    arrays.append(dis((Sx, Sy), (Bx, By)))
    
line = 2_000_000

segments = []

for i, s in enumerate(sensors):
    dx = arrays[i] - abs(s[1] - line)
    if dx < 0:
        continue
    segments.append((s[0] - dx, s[0] + dx))

print(segments)

no_beacon_line = []
for x,y in beacons:
    if line == y:
        no_beacon_line.append(x)

count = 0
left = min(i[0] for i in segments)
right = max(i[1] for i in segments)

for i in range(left, right):
    if i in no_beacon_line:
        continue
    for x,y in segments:
        if x <= i <= y:
            count += 1
            break
print(count+1)
