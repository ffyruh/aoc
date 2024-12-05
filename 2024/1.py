input = open('1.in', 'r')
data = input.read()
input.close()
lines = data.strip().split('\n')

# process lines
def map(str):
    str = str.split('   ')
    str[0] = int(str[0])
    str[1] = int(str[1])
    return str

left, right = [0 for _ in range(len(lines))], [0 for _ in range(len(lines))]
rightDict = {}
for i,line in enumerate(lines):
    left[i], right[i] = map(line)
    rightDict[int(right[i])] = rightDict.get(int(right[i]), 0) + 1

# sort left and right sides
left.sort()
right.sort()

# building up
sum = 0
sim = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])
    sim += left[i] * rightDict.get(left[i], 0)
# p1 answer = 1882714
print(sum)
# p2 answer = 19437052
print(sim)