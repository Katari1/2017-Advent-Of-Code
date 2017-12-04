def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data


def is_valid(list):
    for i in range(len(list)):
        let1=[]
        for letters in list[i]:
            let1.append(letters)
        let1 =sorted(let1)
        words1=[]
        for y in range(len(list)):
            if y == i:
                pass
            else:
                words1.append(list[y])
        for z in words1:
            mom=[]
            for x in z:
                mom.append(x)
            if sorted(mom) == let1:
                return False
    return True

data = parse_input('day4.txt')
count = 0
for i in data:
    if is_valid(i) == True:
        count += 1
print count