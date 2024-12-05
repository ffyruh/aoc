input = open('2.in', 'r')
data = input.read()
input.close()
lines = data.strip().split('\n')

def checkSafe(l,r,which):
    if which > 0:
        if l < r:
            return False
        if abs(l-r) < 1 or abs(l-r) > 3:
            return False
        return True
    elif which < 0:
        if l > r:
            return False
        if abs(l-r) < 1 or abs(l-r) > 3:
            return False
        return True

safe = 0
for line in lines:
    limit = False
    chars = list(map(lambda x: int(x), line.split(' ')))
    # if increasing
    if chars[0] < chars[-1]:
        for i in range(len(chars)-1):
            if not checkSafe(chars[i], chars[i+1], -1):
                # # p1 
                # break
                # p2 
                if limit:
                    break
                if i != 0:
                    if not checkSafe(chars[i-1], chars[i+1], -1):
                        break
            if i == len(chars)-2:
                safe += 1
            limit = not limit
    # if decreasing
    elif chars[0] > chars[-1]:
        for i in range(len(chars)-1):
            if not checkSafe(chars[i], chars[i+1], 1):
                # # p1
                # break
                # p2
                if limit:
                    break
                if i != 0:
                    if not checkSafe(chars[i-1], chars[i+1], 1):
                        break
            if i == len(chars)-2:
                safe += 1
            limit = not limit
    else:
        continue
print(safe)
# p1 = 559, p2 = 601 

# some guy's
# def isok(ls): 
#     # wowowow
#     deltas = [a-b for a,b in zip(ls, ls[1:])]
#     return all(-3 <= n <=-1 for n in deltas) or all(1 <= n <= 3 for n in deltas)

# part_a, part_b = 0,0
# for line in lines:
#     ls = [int(x) for x in line.strip().split()]
#     # wow 
#     part_a += isok(ls)
#     part_b += any(isok(ls[:i]+ls[i+1:]) for i in range(len(ls)))

# print(part_a, part_b)

# 4HbQ's
# print([[*map(int, l.split())] for l in data.strip().split('\n')])
# print([[*map(int, l.split())] for l in open('2.in','r')])

# data = [[*map(int, l.split())] for l in open('2.in','r')]
# f = lambda d: all(1<=a-b<=3 for a, b in zip(d, d[1:]))
# g = lambda d: (d[:i] + d[i+n:] for i in range(len(d)))
# for n in 0,1: print(sum(any(f(e) or f(e[::-1])
#                         for e in g(d)) for d in data))