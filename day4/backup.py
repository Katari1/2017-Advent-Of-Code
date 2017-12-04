def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data


data = parse_input('day4_test.txt')

for i in data:

    print "***************"
    for z in range(len(i)):
        print "The word is: %s" %(i[z]),
        length = len(i[z])
        print "The length is: %s" %(length)
        for v in range(length):
            print "The letters are %s" %(i[z][v])
        for x in i:
            if i[z] == x:
                pass
            else:
                print "Comparing to: %s" %(x),
                length1 = len(x)
                print "The Length is: %s" %(length1)
                for g in range(len(x)):
                    print "The letters are %s" %(x[g])
                    #if length == length1:
                    #    print "Length is Right"
