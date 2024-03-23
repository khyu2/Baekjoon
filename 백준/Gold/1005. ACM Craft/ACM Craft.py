import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(cur):
  if d[cur] != -1: return d[cur]
  d[cur] = time[cur]

  for nxt in a[cur]:
    d[cur] = max(d[cur], time[cur] + dfs(nxt))
  
  return d[cur]

for _ in range(int(input())):
  n, k  = map(int, input().split())
  time = [*map(int, input().split())]
  a = [[] for _ in range(n)]
  d = [-1] * n

  for __ in range(k):
    x, y = map(int, input().split())
    a[y-1].append(x-1)

  w = int(input())
  print(dfs(w-1))