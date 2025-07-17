import sys
input = lambda: sys.stdin.readline().rstrip()

s = {}
d = {'Y': 1, 'F': 2, 'O': 3}
n = input().split()
for i in range(0, int(n[0])):
    s[input()] = 1

print(len(s) // d[n[1]])
