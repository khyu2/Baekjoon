import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]

def is_empty():
  for i in range(n):
    for j in range(m):
      if a[i][j] == 1: return False
  return True

def bfs():
  melt = [[0 for _ in range(m)] for _ in range(n)]
  vis = [[False for _ in range(m)] for _ in range(n)]
  vis[0][0] = True
  q = deque([[0, 0]])

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
      if a[nx][ny] == 1:
        melt[nx][ny] += 1
      elif not vis[nx][ny] and a[nx][ny] == 0:
        q.append([nx, ny])
        vis[nx][ny] = True

  for i in range(n):
    for j in range(m):
      if melt[i][j] > 1: a[i][j] = 0

res = 0
while True:
  bfs()
  res += 1

  if is_empty(): break

print(res)