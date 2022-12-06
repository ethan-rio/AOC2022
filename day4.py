# Part 1
with open("day4.txt", "r") as f:
    lines = f.readlines()
    count = 0
    count_2 = 0
    for line in lines:

        part1, part2 = line.split(',')
        part2 = part2.replace('\n', '')
        num1_1 = int(part1.split('-')[0])
        num1_2 = int(part1.split('-')[1])
        num2_1 = int(part2.split('-')[0])
        num2_2 = int(part2.split('-')[1])
        if (num1_1 <= num2_1 and num1_2 >= num2_2) or (num1_1 >= num2_1 and num1_2 <= num2_2): 
            count += 1
        if (num1_1 <= num2_2) and (num1_2 >= num2_1):
            count_2 += 1
    print(count)
    print(count_2)

