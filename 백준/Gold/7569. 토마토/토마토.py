import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
m, n, h = map(int, input().split())
a = [[[*map(int, input().split())] for _ in range(n)] for _ in range(h)]
vis = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if a[i][j][k] == 1:
        q.append([i, j, k])

while q:
  z, x, y = q.popleft()
  for i in range(6):
    nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h: continue
    if a[nz][nx][ny] == 0 and not vis[nz][nx][ny]:
      q.append([nz, nx, ny])
      vis[nz][nx][ny] = vis[z][x][y] + 1
  
mx = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if vis[i][j][k] == 0 and a[i][j][k] == 0:
        print(-1)
        exit(0)
      else:
        mx = max(mx, vis[i][j][k])

print(mx)