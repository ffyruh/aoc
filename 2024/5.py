# split input in two files
# 5a is rules
input = open('5a.in', 'r')
data = input.read()
input.close()
lines1 = data.strip().split('\n')
# 5b is page ordering
input = open('5b.in', 'r')
data = input.read()
input.close()
lines2 = data.strip().split('\n')

# rule dict buildup
rules = {}
for line in lines1:
    line = line.split('|')
    l,r = int(line[0]), int(line[1])
    rules[l] = rules.get(l, [])
    rules[l].append(r)
lines2 = [list(map(int,line.split(','))) for line in lines2]

# validating a line
def validate(line):
    for i in range(len(line)-1):
        for j in range(i+1,len(line)-1):
            if line[j] not in rules[line[i]]:
                return False
        if i == len(line)-2:
            return True

p1 = 0
p2list = []
for line in lines2:
    if validate(line):
        p1 += line[len(line)//2]
    else: # p2 buildup
        p2list.append(line)
print(p1) # 4637

p2 = 0
for line in p2list:
    while (not validate(line)):
        for i in range(len(line)-1):
            l,r = [], []
            for j in range(i+1,len(line)):
                if line[j] not in rules[line[i]]:
                    l.append(line[j])
                else:
                    r.append(line[j])
            l.append(line[i])
            line = line[:i]+l+r
    p2 += line[len(line)//2]
print(p2) # 6370