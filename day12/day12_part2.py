import re
def parse_input(input):
    data = []
    temp = []
    content = open(input).readlines()
    for i in content:
        a = (re.findall(r'\d+',i))
        a = map(int, a)
        for i in a:
            temp.append(i)
        data.append(list(temp))
        temp=[]
    return data

def create_group(id,data):
    visited=[]
    program_id = id
    visited.append(program_id)
    for z in data:
        if program_id == z[0]:
            pass
        elif program_id in z[1:]:
                visited.append(z[0])
        elif visited in z[1:]:
            visited.append(z[0])
        for i in z[1:]:
            if i in visited and z[0] not in visited:
                visited.append(z[0])
        for x in data:
            for y in x[1:]:
                if y in visited and x[0] not in visited:
                    visited.append(x[0])

    return set(visited)

data = parse_input('day12.txt')
groups = []
newgroups = []
for i in data:
    groups.append(i[0])

while True:
    if len(groups) == 0:
        break
    for i in groups:
        newgroups.append(i)
        results = create_group(i,data)
        for z in results:
            if z in groups:
                groups.remove(z)
            results=[]
print len(newgroups)