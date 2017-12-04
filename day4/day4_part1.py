def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data


data = parse_input('day4.txt')

count = 0
for i in data:
    if len(i) == len(set(i)):
        count += 1

print count
