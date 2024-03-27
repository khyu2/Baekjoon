import sys
input = lambda: sys.stdin.readline().rstrip()

piece = [[0, 0, 0, 1], [0, 1, 2, 1], [0, 0, 0, -1]]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]
vis = [[False] * m for _ in range(n)]
mx = 0

def dfs(x, y, depth, val):
  global mx

  if depth == 4:
    mx = max(mx, val)
    return
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

    if not vis[nx][ny]:
      vis[nx][ny] = True
      dfs(nx, ny, depth + 1, val + a[nx][ny])
      vis[nx][ny] = False

def get_point(i, j, p, q):
  res = 0
  for dx, dy in zip(p, q):
    nx, ny = i + dx, j + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m: return 0
    res += a[nx][ny]
  return res

def place(i, j):
  ret = 0

  dfs(i, j, 0, 0)
  ret = max(ret, mx)
  ret = max(ret, get_point(i, j, piece[0], piece[1])) # ㅜ
  ret = max(ret, get_point(i, j, piece[2], piece[1])) # ㅗ
  ret = max(ret, get_point(i, j, piece[1], piece[0])) # ㅏ
  ret = max(ret, get_point(i, j, piece[1], piece[2])) # ㅓ
  
  return ret


res = 0
for i in range(n):
  for j in range(m):
    res = max(res, place(i, j))

print(res)