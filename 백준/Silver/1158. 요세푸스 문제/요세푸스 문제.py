import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
q = deque([(i + 1) for i in range(n)])
a = []

i = 1
while len(q):
  if i == k: 
    a.append(q.popleft())
    i = 1
  else: 
    q.append(q.popleft())
    i += 1

print('<', end='')
print(*a, sep=', ', end='>')