import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().rstrip().split())
vis = [[0 for _ in range(m)] for _ in range(n)]
a = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

for i in range(n):
  for j, x in enumerate(map(int, input().rstrip().split())):
    if x == 2:
      q.append((i, j))
    a[i][j] = x

while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if a[nx][ny] == 1 and not vis[nx][ny]:
      vis[nx][ny] = vis[x][y] + 1
      q.append((nx, ny))

for i in range(n):
  for j in range(m):
    if a[i][j] == 1 and not vis[i][j]:
      vis[i][j] = -1
  
for i in range(n):
  for j in range(m):
    print(vis[i][j], end=" ")
  print()