import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
ans = 0
a = []
vis = [[False for _ in range(m)] for _ in range(n)]
q = deque()

for i in range(n):
  x = input()
  a.append(x)
  for j in range(m):
    if x[j] == 'I':
      q.append([i, j])
      vis[i][j] = True

while q:
  x, y = q.popleft()
  if a[x][y] == 'P': ans += 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or vis[nx][ny]: continue
    if a[nx][ny] == 'O' or a[nx][ny] == 'P':
      q.append([nx, ny])
      vis[nx][ny] = True
  
print(ans if ans else 'TT')