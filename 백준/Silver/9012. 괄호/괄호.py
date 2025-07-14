import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(0, int(input())):
    a = []
    p = False
    for j in input():
        if j == '(': a.append(j)
        elif j == ')':
            if len(a) and a[-1] == '(': a.pop()
            else:
                p = True
                break
    print('NO' if p or len(a) != 0 else 'YES')