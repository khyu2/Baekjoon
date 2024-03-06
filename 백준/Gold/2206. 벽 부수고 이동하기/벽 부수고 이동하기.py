import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
a = [input() for _ in range(n)]
vis = [[[0, 0] for _ in range(m)] for _ in range(n)] # x, y, dist, destroyed

def bfs():
  q = deque([[0, 0, False]]) # start_x, start_y, destroyed
  vis[0][0][0] = 1

  while q:
    x, y, destroyed = q.popleft()

    if x == n - 1 and y == m - 1: return vis[x][y][destroyed]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m or vis[nx][ny][destroyed]: continue

      if a[nx][ny] == '1' and not destroyed: # 벽이고 아직 부수지 않았다면
        q.append([nx, ny, 1])
        vis[nx][ny][1] = vis[x][y][destroyed] + 1
      elif a[nx][ny] == '0': # 벽이 아니라면
        q.append([nx, ny, destroyed])
        vis[nx][ny][destroyed] = vis[x][y][destroyed] + 1
  
  return -1

print(bfs())

# for i in range(n):
#   for j in range(m):
#     print('[', vis[i][j][0], vis[i][j][1], ']', end=' ')
#   print()