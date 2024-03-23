import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def topological_sort(a, in_degrees, n, w):
  q = deque()

  for i, degree in enumerate(in_degrees):
    if degree == 0: q.append(i)

  res = [0] * n
  while q:
    u = q.popleft()

    for v in a[u]:
      in_degrees[v] -= 1
      res[v] = max(res[v], res[u] + time[u])

      if in_degrees[v] == 0:
        q.append(v)
    
  return res[w-1] + time[w-1]

for _ in range(int(input())):
  n, k = map(int, input().split())
  time = [*map(int, input().split())]
  in_degrees = [0] * n
  a = [[] for _ in range(n)]

  for __ in range(k):
    x, y = map(int, input().split())
    a[x-1].append(y-1)
    in_degrees[y-1] += 1
  
  w = int(input())

  print(topological_sort(a, in_degrees, n, w))