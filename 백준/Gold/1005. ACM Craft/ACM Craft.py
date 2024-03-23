import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def topological_sort(a, in_degrees, n):
  q = deque()

  for i, degree in enumerate(in_degrees):
    if degree == 0: q.append(i)

  res = []
  while q:
    u = q.popleft()
    res.append(u)

    for v in a[u]:
      in_degrees[v] -= 1
      if in_degrees[v] == 0:
        q.append(v)
    
  return res

def cal_building_time(a, in_degrees, n, w): # 위상 정렬 결과, 크기, 목적지
  res = [0] * n
  for u in topological_sort(a, in_degrees, n):
    for v in a[u]:
      res[v] = max(res[v], res[u] + time[u])

  # print(res)
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

  print(cal_building_time(a, in_degrees, n, w))