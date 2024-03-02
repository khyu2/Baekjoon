import sys
import math
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
  x, y, z = map(int, input().rstrip().split())
  a[x].append([y, z])

def spfa(start):
  dist = [math.inf] * (n + 1)
  vis = [0] * (n + 1)
  inQ = [False] * (n + 1)

  q = deque([start])
  dist[start] = 0
  inQ[start] = True
  vis[start] += 1

  while q:
    cur = q.popleft()
    inQ[cur] = False

    for v, w in a[cur]:
      if dist[v] > dist[cur] + w:
        dist[v] = dist[cur] + w

        if not inQ[v]:
          q.append(v)
          inQ[v] = True
          vis[v] += 1
          if vis[v] >= n:
            return []
          
  return dist[2:]

dist = spfa(1)
if dist:
  for i in dist:
    print(i if i != math.inf else -1)
else:
  print(-1)
