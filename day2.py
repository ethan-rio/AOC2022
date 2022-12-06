game_map = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3, # Scissor
    'X': 1, # Rock -> LOSE
    'Y': 2, # Paper -> DRAW
    'Z': 3 # Scissor -> WIN
}
def rules1(op, me):
    # draw
    if op == me:
        return me + 3
    
    # Win
    if (me - op) in [1, 1, -2]:
        return me + 6
    return me

def rules2(op, me):
    # DRAW
    if me == 2:
        return op + 3
    
    # WIN
    if me == 3:
        q = (op + 1) // 3
        r = (op + 1)%3
        if r == 0:
            return 3*q + 6
        else:
            return r + 6
    
    # LOSE
    if me == 1:
        r = op + 2
        if r <= 3:
            return 3
        else:
            return r%3

with open("day2.txt", "r") as f:
    lines = f.readlines()
    temp = 0
    days = []
    for line in lines:
        op = line[0]
        me = line[2]
        # print(game_map[op], game_map[me])
        days.append(rules2(game_map[op], game_map[me]))
        # sum += rules(game_map[op], game_map[me])
        # print(sum)
    # print(sum)
    print(days)
    print(sum(days))

