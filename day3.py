# Part 1
with open("day3.txt", "r") as f:
    lines = f.readlines()
    temp = 0
    for line in lines:
        first = line[0:int((len(line)-1)/2)]
        second = line[int((len(line)-1)/2): -1]
    
        a=list(set(first)&set(second))
        common_char = a[0]
        if common_char.islower():
            temp += ord(common_char) - 96
        else:
            temp += ord(common_char) - 38
    
    print(temp)

# Part 2
with open("day3.txt", "r") as f:
    lines = f.readlines()
    temp = 0
    for i in range(0, len(lines)):
        if i % 3 == 0:
            l1 = lines[i]
            l2 = lines[i+1]
            l3 = lines[i+2]
            a=list(set(l1)&set(l2)&set(l3))
            a.remove('\n')
            common_char = a[0]
            if common_char.islower():
                temp += ord(common_char) - 96
            else:
                temp += ord(common_char) - 38
    
    print(temp)