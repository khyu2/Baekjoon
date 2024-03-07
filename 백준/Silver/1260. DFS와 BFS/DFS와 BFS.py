import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
a = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)

for i in range(m):
  x, y = map(int, input().split())
  a[x].append(y)
  a[y].append(x)

for i in range(n + 1):
  a[i].sort()

def dfs(cur):
  if vis[cur]: return
  vis[cur] = True

  print(cur, end=' ')
  for i in a[cur]:
    if not vis[i]:
      dfs(i)

def bfs(start):
  q = deque([start])
  vis[start] = True

  while q:
    cur = q.popleft()
    print(cur, end=' ')
    
    for i in a[cur]:
      if not vis[i]:
        vis[i] = True
        q.append(i)

dfs(v)
print()
vis = [False] * (n + 1)

bfs(v)