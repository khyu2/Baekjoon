import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def topological_sort(a, n): # 0-index
  in_degrees = [0] * n
  q = deque()
  
  for u in range(n): 
    for v in a[u]:
      in_degrees[v] += 1

  for i, x in enumerate(in_degrees): # 차수가 0 인 노드 큐에 삽입
    if x == 0: q.append(i)

  res = []
  while q:
    u = q.popleft()
    res.append(u)

    for v in a[u]:
      in_degrees[v] -= 1

      if in_degrees[v] == 0:
        q.append(v)
  
  return res
    
n, m = map(int, input().split())
a = [[] for _ in range(n)]
for i in range(m):
  x, y = map(int, input().split())
  a[x-1].append(y-1)

res = topological_sort(a, n)
for i in res: print(i + 1, end=' ')