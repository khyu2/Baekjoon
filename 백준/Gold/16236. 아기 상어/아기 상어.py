import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n = int(input())
sx, sy, sz = 0, 0, 2 # shark_x, shark_y, shark_size
a = []

for i in range(n):
  a.append([*map(int, input().split())])
  for j, x in enumerate(a[i]):
    if x == 9:
      sx, sy = i, j
      a[i][j] = 0

def find():
  q = deque([[sx, sy]])

  food = []
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n or vis[nx][ny]: continue
      if a[nx][ny] <= sz:
        vis[nx][ny] = vis[x][y] + 1
        q.append([nx, ny])
      # print('nx, ny:', nx, ny)
      if a[nx][ny] and sz > a[nx][ny]: # 먹이가 상어보다 작다면
        food.append([vis[nx][ny], nx, ny])

  return food

res = 0
food_cnt = 0
while True:
  vis = [[0 for _ in range(n)] for _ in range(n)]
  food = find()

  if food: # 먹을 수 있다면
    food.sort() # [거리, (x, y)] 순 정렬
    
    res += food[0][0]
    sx, sy = food[0][1], food[0][2]
    a[sx][sy] = 0
    food_cnt += 1
    
    if food_cnt == sz:
      sz += 1
      food_cnt = 0
    # print(food[0])
    # for i in range(n):
    #   for j in range(n):
    #     print(a[i][j], end=' ')
    #   print()
  else: break

print(res)