def parse_input(puzzle_input):
    data=[]
    content = open(puzzle_input,'r')
    lines = content.readlines()
    for l in lines:
        if l.strip():
            data.append(l.strip().split('\t'))
    return data

a = parse_input('day2.txt')
sum = 0
for i in a:
    diff = 0
    ints=[]
    for z in i:
        ints.append(int(z))
        ints = sorted(set(ints))
    for z in range(len(ints)):
        #print ints[z],
        for y  in ints:
            if ints[z] == y:
                pass
            elif ints[z] % y == 0:
                print ints[z],
                print y
                sum += ints[z] / y
print sum
