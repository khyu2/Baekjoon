import sys
import math
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [[] for _ in range(n + 1)]
distance = [math.inf] * (n + 1)

for _ in range(m):
  u, v, w = map(int, input().rstrip().split())
  a[u-1].append([v-1, w])

def bellman_ford(s): # return True if minusCycle exists
  distance[s] = 0

  for i in range(n):
    for j in range(n):
      for nxt, dst in a[j]: # u -> v : w
        if distance[j] != math.inf and distance[nxt] > distance[j] + dst:
          distance[nxt] = distance[j] + dst
          if i == n - 1: return True

  return False

minus_cycle = bellman_ford(0)

if minus_cycle:
  print(-1)
else:
  for i in range(1, n):
    print(distance[i] if distance[i] != math.inf else -1)
