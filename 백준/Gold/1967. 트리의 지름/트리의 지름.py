import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
a = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)
ans = 0
idx = 0

for i in range(n - 1):
  x, y, z = map(int, input().rstrip().split())
  a[x].append([y, z])
  a[y].append([x, z])

def dfs(cur, w):
  global ans
  global idx

  if vis[cur]:
    return
  vis[cur] = True

  if ans < w:
    ans = w
    idx = cur
  
  for nxt, nw in a[cur]:
    if not vis[nxt]:
      dfs(nxt, w + nw)

dfs(1, 0)

ans = 0
vis = [False] * (n + 1)

dfs(idx, 0)

print(ans)