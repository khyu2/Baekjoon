import sys
input = lambda: sys.stdin.readline().rstrip()

a = [0]
n, s, p = map(int, input().split())
if n != 0: a = [*map(int, input().split())]

cnt = 1
for i in a:
    if i > s: cnt += 1

if n < p: print(cnt)
else:
    if a[-1] < s: print(cnt)
    else: print(-1)