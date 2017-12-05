def parse_input(location):
    data=[]
    content = open(location).read().split()
    for l in content:
        data.append(int(l))
    return data

def process_steps(maze):
    step = 0
    pos = 0
    while pos  < len(maze) > 0:
        #print maze
        #print "Step %s" % (step)
        #print "Pos: %s" % (maze[pos])
        jump = maze[pos]
        #print "Updating maze"
        if jump >= 3:
            maze[pos] -= 1
        else:
            maze[pos] += 1
        #print "We are jumping: %s" % (jump)
        pos += jump
        #print "Updating Step"
        step += 1
        #print step
        #print maze
        try:
            maze[pos]
        except:
            return step



data = parse_input('day5.txt')
total = process_steps(data)
print total