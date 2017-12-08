import operator
def parse_input(location):
    content=open(location).readlines()
    content = [x.strip().split(' ') for x in content]
    return content

def does_exist(results,letter):
    if letter in results:
        return True
    else:
        return False
def compare_condition(let,op,value):
    ops = {"+": operator.add, "-": operator.sub, '>=': operator.ge, '<=': operator.le, '==': operator.eq, '!=':operator.ne, '>': operator.gt, '<': operator.lt}
    return ops[op](let,value)

results={}
data = parse_input('day8.txt')
for i in data:
    perform = {'inc': operator.add, 'dec': operator.sub}
    let = i[0]
    instr = i[1]
    modifier = int(i[2])
    variable = i[4]
    action = i[5]
    value = int(i[6])
    if does_exist(results,let):
        pass
    else:
        results[let] = 0
    if does_exist(results,variable):
        pass
    else:
        results[variable] = 0
    if compare_condition(results[variable],action,value):
        results[let] = perform[instr](results[let],modifier)
    else:
        pass

print results[max(results, key=results.get)]

