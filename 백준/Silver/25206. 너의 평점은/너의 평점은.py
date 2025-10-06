import sys

input = lambda: sys.stdin.readline().rstrip()

a = [input() for _ in range(20)]
grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': '1.5', 'D0': 1.0, 'F': 0, 'P': 0}

score = 0
cnt = 0
for i in a:
    x, y, z = i.split(' ')
    if z == 'P': continue
    score += int(float(y)) * float(grade[z])
    cnt += int(float(y))

print(score / cnt)


