import sys
import math
import heapq as hq
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
s = int(input().rstrip())
a = [[] for _ in range(v + 1)]
q = []

for i in range(e):
  x, y, z = map(int, input().rstrip().split())
  a[x].append([y, z])

def dijkstra(s):
  d = [math.inf] * (v + 1)
  d[s] = 0
  hq.heappush(q, (0, s))

  while q:
    cost, cur = hq.heappop(q)
    if d[cur] >= cost:
      for nxt, w in a[cur]:
        nCost = cost + w
        if d[nxt] > nCost:
          d[nxt] = nCost
          hq.heappush(q, (nCost, nxt))
  
  return d

for i in dijkstra(s)[1:]:
  print(i if i != math.inf else 'INF')