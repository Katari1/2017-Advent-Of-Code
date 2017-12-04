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
    lowest = ints[0]
    highest = ints[-1]
    print "The highest number is: %s" %(highest),
    print "The lowest number is %s" %(lowest),
    diff = (highest - lowest)
    sum += diff
    print "The difference is %s" %(diff)
print sum
