import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
a = [input() for _ in range(n)]
vis = [[0] * m for _ in range(n)]
q = deque([[0, 0]])
vis[0][0] = 1

while q:
  x, y = q.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
    if a[nx][ny] == '1' and not vis[nx][ny]:
      q.append([nx, ny])
      vis[nx][ny] = vis[x][y] + 1

print(vis[n-1][m-1])