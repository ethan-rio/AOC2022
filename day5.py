import re
with open("day5.txt", "r") as f:
    data = [l.rstrip() for l in f.readlines()]

empty_line_index = data.index('')
stack_data = data[:empty_line_index]
# moves = [re.sub('\D', '', line) for line in data[empty_line_index+1:]]
moves = data[empty_line_index+1:]
init_stacks = []

stack_size = int(stack_data[-1][-1])
for i in range(0, stack_size):
    init_stacks.append([])
print(stack_data)


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

for line in stack_data:
    print("LINE: ", line)
    for c in line:
        if c.isalpha():
            index = indices(line, c)
            line = line.replace(c, ' ')
            for i in index:
                init_stacks[int((i-1)/4)].insert(0, c)    


def extract_move(move):
    split = move.split(" ")
    return int(split[1]), int(split[3]) - 1, int(split[5]) - 1 



def do_move(move, stacks):
    count, from_stack, to_stack = extract_move(move)
    # print(count, from_stack, to_stack)
    for i in range(0, count):
        temp = stacks[from_stack].pop()
        stacks[to_stack].append(temp)
    
    # for i in stacks:
    #     print(i)
    # print("-----")
    return stacks

# for move in moves:
#     stack_1 = do_move(move, init_stacks)

# for stack in stack_1:
#     print(stack[-1])

def do_move_2(move, stacks):
    count, from_stack, to_stack = extract_move(move)
    temp = stacks[from_stack][0 - count:]
    stacks[to_stack] += temp
    for i in range(0, count):
        stacks[from_stack].pop()
    return stacks

for move in moves:
    stack_2 = do_move_2(move, init_stacks)

print("PART 2")
for stack in stack_2:
    print(stack[-1])