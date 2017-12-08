def parse_input(location):
    data=[]
    content = open(location).readline().split()
    for l in content:
        data.append(int(l))
    return data

def get_history(location):
    data=[]
    content = open(location).readline().split()
    data.append(content)
    data=[[int(j) for j in i] for i in data]
    return data

def get_max(data):
    data=sorted(set(data))
    max = data[-1]
    return max

def find_location(data,value):
    location = data.index(value)
    return location

def reallocate_bank(data):
    #print "Getting Max Entry"
    max = get_max(data)
    #print max
    location = find_location(data,max)
    #print "Location in List: %s" %(location)
    data[location] = 0
    #print "Clearing Max Value"
    #print "Distributing to array"
    location += 1
    for i in range(max):
        if max > 0 and location < len(data):
            #print "Max: %s" %max
            #print "Data: %s" %data
            #print "Location: %s" %location
            data[location] += 1
            location += 1
            max -= 1
        elif max > 0 and location == len(data):
            location = 0
            #print "Max: %s" % max
            #print "Data: %s" % data
            #print "Location: %s" % location
            data[location] += 1
            location += 1
            max -= 1
        #print "Data: %s" % data
        #print "Location: %s" % location
    return data

def check_duplicate(data,history):
    if len(history) == 1:
        return False
    elif data in history:
        return True
    else:
        return False

data = parse_input('day6.txt')
history = get_history('day6.txt')
count = 1
while True:
    data = reallocate_bank(data)
    if check_duplicate(data,history):
        break
    history.append(list(data))
    count += 1
print count
