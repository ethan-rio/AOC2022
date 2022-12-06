with open("day1.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

deer_list = []
sum_deer = 0
for line in lines:
    if line != '':
        sum_deer = int(line) + sum_deer
    else:
        deer_list.append(sum_deer)
        sum_deer = 0

deer_list.sort(reverse=True)
print(deer_list[0])
print(deer_list[0] + deer_list[1] + deer_list[2])