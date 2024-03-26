import sys
import math
import heapq
input = lambda: sys.stdin.readline().rstrip()

def dijkstra(s):
  res = [1e9] * (n + 1)
  res[s] = 0
  q = [(0, s)]

  while q:
    w, u = heapq.heappop(q)

    for v, cost in a[u]: 
      cost += w
      if res[v] > cost:
        res[v] = cost
        heapq.heappush(q, (cost, v))

  return res

for _ in range(int(input())):
  n, m, t = map(int, input().split())
  s, g, h = map(int, input().split())
  a = [[] for _ in range(n + 1)]

  for __ in range(m):
    u, v, w = map(int, input().split())
    a[u].append([v, w])
    a[v].append([u, w])

  s_start = dijkstra(s)
  g_start = dijkstra(g)
  h_start = dijkstra(h)

  res = []
  for i in range(t):
    x = int(input())
    if s_start[x] == s_start[g] + g_start[h] + h_start[x]: res.append(x)
    elif s_start[x] == s_start[h] + h_start[g] + g_start[x]: res.append(x)
  print(*sorted(res))