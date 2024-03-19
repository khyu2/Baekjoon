import sys
import math
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
chicken = []
house = []
out = []
vis = [False] * (1000)

for i in range(n):
  for j, x in enumerate(list(map(int, input().split()))):
    if x == 1: house.append([i, j])
    elif x == 2: chicken.append([i, j])

res = math.inf
def dfs(idx):
  global res

  if len(out) == m:
    dist = [[math.inf] * n for _ in range(n)]

    for i, [r, c] in enumerate(out): # 각 치킨집에서
      for j, [x, y] in enumerate(house): # 집집마다 거리 확인
        dist[x][y] = min(dist[x][y], abs(r - x) + abs(c - y))
    
    tmp = 0
    for i in range(n):
      for j in range(n):
        if dist[i][j] != math.inf: tmp += dist[i][j]
    res = min(res, tmp)

    # print()
    # for i in range(n):
    #   for j in range(n):
    #     print(dist[i][j] if dist[i][j] != math.inf else 0, end=' ')
    #   print()

  else:
    for i in range(idx, len(chicken)):
      if not vis[i]:
        vis[i] = True
        out.append(chicken[i])
        dfs(i)
        out.pop()
        vis[i] = False

dfs(0)
print(res)