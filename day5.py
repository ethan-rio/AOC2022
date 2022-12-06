import re
with open("day5.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

empty_line_index = data.index('')
stack_data = data[:empty_line_index]
# moves = [re.sub('\D', '', line) for line in data[empty_line_index+1:]]
moves = data[empty_line_index+1:]
stacks = []

stack_size = int(stack_data[-1][-1])
for i in range(0, stack_size):
    stacks.append([])
print(stacks)


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

for line in stack_data:
    print("LINE: ", line)
    for c in line:
        if c.isalpha():
            index = indices(line, c)
            line = line.replace(c, ' ')
            for i in index:
                stacks[int((i-1)/4)].insert(0, c)    

print(stacks)
print(moves)

def extract_move(move):
    split = move.split(" ")
    return split[1], split[3], split[5]


def do_move(move, stacks):
    count, from_stack, to_stack = extract_move(move)
    print(count, from_stack, to_stack)
    for i in range(0, count):
        temp = stacks[from_stack].pop()
        stacks[to_stack].append(temp)
    
    return stacks

for move in moves:
    stacks = do_move(move, stacks)

print(stacks)