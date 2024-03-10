import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
back_dx = [1, 0, -1, 0]
back_dy = [0, -1, 0, 1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
clean = [[False] * m for _ in range(n)]
q = deque([[r, c, d]])

def get_dir(d):
  return d - 1 if d else 3

def get_back_dir(d):
  if d == 0: return 2
  if d == 1: return 3
  if d == 2: return 0
  return 1

def back_check(x, y, d):
  nx = x + back_dx[d]
  ny = y + back_dy[d]
  if nx < 0 or nx >= n or ny < 0 or ny >= m: return False
  if a[nx][ny]: return False
  return True

ans = 0
while q:
  x, y, d = q.popleft()
  # print(x, y, d)

  if not clean[x][y]: 
    clean[x][y] = True
    ans += 1
  
  is_clean = False
  for i in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    d = get_dir(d)
    # print('nx, ny', nx, ny)
    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
    if a[nx][ny] == 0 and not clean[nx][ny]:
      clean[nx][ny] = True
      is_clean = True
      q.append([nx, ny, d])
      ans += 1
      break
  
  if not is_clean: # 상하좌우에 청소할 곳이 없다면
    if back_check(x, y, d): # 뒤로 이동할 수 있다면
      nx = x + back_dx[d]
      ny = y + back_dy[d]
      q.appendleft([nx, ny, d]) # 방향 그대로 뒤로 후진
    else:
      break

print(ans)
