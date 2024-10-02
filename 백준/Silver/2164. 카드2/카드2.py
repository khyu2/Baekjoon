import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = deque([(i + 1) for i in range(n)])

while len(q) > 1:
  q.popleft()

  if len(q) == 1: break

  q.append(q.popleft())

print(q[0])