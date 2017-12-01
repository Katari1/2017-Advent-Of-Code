def parse_input(puzzle_input):
    data=[]
    content = open(puzzle_input).read()
    lines = content.strip()
    for l in lines:
        if l.strip():
            data.append(int(l))
    return data




parsed_input = parse_input('day1.txt')
sum = 0
position = 0
for i in range(len(parsed_input)):
    try:
        current =  parsed_input[i]
        next = parsed_input[i+1]
    except IndexError:
        current = parsed_input[i]
        remaining = parsed_input[0]
    if current == next:
        sum += current
print sum