from collections import deque

x, y = map(int, input().split())
a = {}
q = deque([x])
a[x] = 1

cnt = 0
while len(q):
    x = q.pop()
    for nx in (x * 2, int(str(x) + '1')):
        if nx > y: continue
        if nx not in a or a[x] + 1 < a[nx]:
            a[nx] = a[x] + 1
            q.append(nx)

print(a[y] if y in a and a[y] != 0 else -1)

