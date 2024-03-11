import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
a = [input() for _ in range(n)]
vis = [[False] * n for _ in range(n)]

def bfs(i, j):
  q = deque([[i, j]])
  vis[i][j] = True

  ret = 1
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
      if a[nx][ny] == '1' and not vis[nx][ny]:
        ret += 1
        q.append([nx, ny])
        vis[nx][ny] = True

  return ret

component = 0
count = []
for i in range(n):
  for j in range(n):
    if a[i][j] == '1' and not vis[i][j]:
      component += 1
      count.append(bfs(i, j))

print(component)
print(*sorted(count), sep='\n')