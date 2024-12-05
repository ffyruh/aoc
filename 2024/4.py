input = open('4.in', 'r')
data = input.read()
input.close()
# convert to 2d matrix
lines = [list(line) for line in data.strip().split('\n')]

# lines = ['XMASXMAS',
#         'MMMMMMMM',
#         'AAAAAAAA',
#         'SSSSSSSS',
#         'SSSSSSSS',
#         'AAAAAAAA',
#         'MMMMMMMM',
#         'XMASXMAS']

# print(lines)
p1 = 0
for i in range(len(lines)):
    # 3 136 136 136
    for j in range(len(lines)):
        # horizontal
        if j <= 136:
            hori = lines[i][j]+lines[i][j+1]+lines[i][j+2]+lines[i][j+3]
            if hori == 'XMAS' or hori == 'SAMX':
                p1 += 1
        # vertical
        if i <= 136:
            vert = lines[i][j]+lines[i+1][j]+lines[i+2][j]+lines[i+3][j]
            if vert == 'XMAS' or vert == 'SAMX':
                p1 += 1
        # rising diagonal
        if j >= 3 and i <= 136:
            riseDiag = lines[i][j]+lines[i+1][j-1]+lines[i+2][j-2]+lines[i+3][j-3]
            if riseDiag == 'XMAS' or riseDiag == 'SAMX':
                p1 += 1
        # receding diagonal 
        if j <= 136 and i <= 136:
            recDiag = lines[i][j]+lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3]
            if recDiag == 'XMAS' or recDiag == 'SAMX':
                p1 += 1
print(p1) # 2297


p2 = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i <= 137 and j <= 137:
            shape = lines[i][j]+lines[i][j+2]+lines[i+1][j+1]+lines[i+2][j]+lines[i+2][j+2]
            if shape == 'MMASS': # up
                p2 += 1
            elif shape == 'SSAMM': # down
                p2 += 1
            elif shape == 'MSAMS': # left
                p2 += 1
            elif shape == 'SMASM': # right
                p2 += 1
print(p2) # 1745

