import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = [-1] * 200001
q = deque([n])
a[n] = 0

while q:
  cur = q.popleft()
  if cur == k: break

  for i in (cur * 2, cur - 1, cur + 1):
    if 0 <= i <= 100000 and a[i] == -1:
      if i == cur * 2:
        a[i] = a[cur]
      else:
        a[i] = a[cur] + 1
      q.append(i)

print(a[k])
# print(a[1], a[2], a[4], a[5], a[10], a[40], a[39], a[624], a[625], a[10000])