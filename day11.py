from collections import defaultdict
import numpy as np
with open("day11.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


monkeys = []
cur_monkey = 0
cur_items = []
cur_op = ''
cur_div = 0
cur_true = 0
cur_false = 0
for line in lines:
    parts = line.split(" ")
    if parts[0] == 'Monkey':
        m_index = parts[1].split(":")
        m_index = int(m_index[0])
        monkeys.append([])
        cur_monkey = m_index
    
    if parts[0] == "Starting":
        items = []
        temp_parts = line.split(": ")
        item_string = temp_parts[1].split(", ")
        for i in item_string:
            items.append(int(i))
        cur_items = items
    if parts[0] == "Operation:":
        op = line.split(": ")[1]
        op = op.split("=")[-1].strip()
        op = op.split(" ")
        cur_op = ''.join(op)
    if parts[0] == "Test:":
        div = int(parts[-1])
        cur_div = div
    if parts[0] == "If":
        if parts[1] == "true:":
            true = int(parts[-1])
            cur_true = true
        if parts[1] == "false:":
            false = int(parts[-1])
            cur_false = false
            monkeys.append([cur_items, cur_op, cur_div, cur_true, cur_false])

monkeys = [m for m in monkeys if m != []]

LCM = 1

for m in monkeys:
    LCM *= LCM * m[2]

counts = [0 for _ in range(len(monkeys))]
items_monkey_list = [monkey[0] for monkey in monkeys]
part = 2
rounds = 20 if part == 1 else 10000
for i in range(rounds):
    for j in range(len(monkeys)):
        items = items_monkey_list[j]
        div = monkeys[j][2]
        true = monkeys[j][-2]
        false = monkeys[j][-1]
        for item in items:
            counts[j] += 1
            temp_op = lambda old,op=op:eval(monkeys[j][1])
            item = temp_op(item)
            # print(item)
            if part == 1:
                item = item // 3
            else:
                item %= LCM
            if item % div != 0:
                items_monkey_list[false].append(item)
            else:
                items_monkey_list[true].append(item)
        items_monkey_list[j] = []
    
print(f"PART {part}: ", sorted(counts)[-1] * sorted(counts)[-2])