import re
with open("day6.txt", "r") as f:
    line = f.readline()
# line = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def is_distinct(input_str):
    for c in input_str:
        if input_str.count(c) > 1:
            return False
    return True



for i in range(14, len(line)):
    seg = line[i-14: i]
    if is_distinct(seg):
        print(seg)
        print(i)
        break