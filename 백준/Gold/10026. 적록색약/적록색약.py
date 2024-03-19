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
  color = a[i][j]

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n or vis[nx][ny]: continue
      if a[nx][ny] == color:
        q.append([nx, ny])
        vis[nx][ny] = True

def get_component():
  comp = 0
  for i in range(n):
    for j in range(n):
      if not vis[i][j]:
        bfs(i, j)
        comp += 1

  return comp

print(get_component())

for i in range(n):
  a[i] = a[i].replace('R', 'G')
vis = [[False] * n for _ in range(n)]

print(get_component())