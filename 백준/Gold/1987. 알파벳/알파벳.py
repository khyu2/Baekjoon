import sys
input = lambda: sys.stdin.readline().rstrip()

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
a = [input() for _ in range(n)]
d = [0 for _ in range(26)]
count = 1

def dfs(x, y, k):
  global count
  count = max(count, k)

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
    if not d[ord(a[nx][ny]) - 65]:
      d[ord(a[nx][ny]) - 65] = 1
      dfs(nx, ny, k + 1)
      d[ord(a[nx][ny]) - 65] = 0

d[ord(a[0][0]) - 65] = 1
dfs(0, 0, 1)
print(count)