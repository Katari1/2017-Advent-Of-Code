def parse_input(puzzle_input):
    data=[]
    content = open(puzzle_input).read()
    lines = content.strip()
    for l in lines:
        if l.strip():
            data.append(int(l))
    return data



sum = 0
parsed_input = parse_input('day1.txt')
ptc = len(parsed_input) /2

for i in range(len(parsed_input)):
    try:
        current =  parsed_input[i]
        next = parsed_input[i+ptc]
    except IndexError:
        current = parsed_input[i]
        check = (i+ptc) - len(parsed_input)
        next = parsed_input[check]
    if current == next:
        sum += current
print sum