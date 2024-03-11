import sys
import math
import heapq
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]

def dijkstra(s):
  d = [math.inf] * (n + 1)
  q = []
  heapq.heappush(q, (0, s)) # dist, node
  d[s] = 0

  while q:
    dst, u = heapq.heappop(q)

    if dst > d[u]: continue
    
    for v, w in a[u]:
      nDst = dst + w
      if d[v] > nDst:
        d[v] = nDst
        heapq.heappush(q, ( nDst,v ))
  
  return d

for _ in range(m):
  u, v, w = map(int, input().split())
  a[u].append([v, w])
  a[v].append([u, w])

v1, v2 = map(int, input().split())

ans1, ans2 = dijkstra(1)[v1], dijkstra(1)[v2]
ans1 += dijkstra(v1)[v2]
ans2 += dijkstra(v2)[v1]
ans1 += dijkstra(v2)[n]
ans2 += dijkstra(v1)[n]

ans = min(ans1, ans2)
print(ans if ans != math.inf else -1)

