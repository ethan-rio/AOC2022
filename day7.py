from collections import defaultdict

with open("day7.txt", "r") as f:
    data = '\n' + f.read().strip()
    cmd_boxes = data.split("\n$ ")[1:]

dir_map = []

dir_sizes = defaultdict(int)
dir_dict = defaultdict(list)

# PART 1
def extract(box):
    lines = box.split('\n')
    cmd = lines[0]
    out = lines[1:]
    print("CMD: ", cmd)
    print("OUT: ", out)

    cmd_type = cmd.split(" ")[0]
    if cmd_type == 'cd':
        if cmd.split(" ")[1] != '..':
            dir_map.append(cmd.split(" ")[1])
        else: 
            dir_map.pop()
        return
    
    else:
        path = "/".join(dir_map)
        sizes = []
        for i in out:
            v1, v2 = i.split(" ")
            if v1 == 'dir':
                temp = path + '/' + v2
                dir_dict[path].append(temp)
            else:
                sizes.append(int(v1))

    dir_sizes[path] = sum(sizes)


for box in cmd_boxes:
    extract(box)

def DFS(path):
    size = dir_sizes[path]
    for c in dir_dict[path]:
        size += DFS(c)
    return size

total = 0
for path in dir_sizes:
    if DFS(path) <= 100000:
        total += DFS(path)

print(total)

# PART 2

need = DFS("/") - 40000000

ans = 9999999999999999999999
for path in dir_sizes:
    size = DFS(path)
    if size >= need:
        ans = min(ans, size)

print(ans)