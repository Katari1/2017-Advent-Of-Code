data = [0,1,2,3,4]
jumps = [3,4,1,5]

def reverse_list(data,pos,length):
    temp=[]
    if pos + length >= len(data):
        for i in range(length):
            temp.append(data[(i + pos) % len(data)])
        temp = list(reversed(temp))
        for i in range(len(temp)):
            data[(i + pos) % len(data)] = temp[i]
    else:
        data[pos:(pos + length)] = reversed(data[pos:(pos + length)])
    return data

def create_list():
    data = []
    for i in range(256):
        data.append(i)
    return data

def parse_input(info):
    data=[]
    content = open(info).readline()
    for i in content.split(','):
            data.append(int(i))
    return data

pos = 0
skip_size=0
data = create_list()
jumps = parse_input('day10.txt')

for i in range(len(jumps)):
    length = jumps[i]
    data = reverse_list(data,pos,length)
    pos += ((length + skip_size) % len(data))
    skip_size += 1

print "The Result of Multiplying The First Two Numbers is: %s" %(data[0] * data[1])
