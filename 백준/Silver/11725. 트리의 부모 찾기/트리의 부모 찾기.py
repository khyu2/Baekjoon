import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
a = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)
parent = [0] * (n + 1)

for i in range(n - 1):
  x, y = map(int, input().rstrip().split())
  a[x].append(y)
  a[y].append(x)

def dfs(cur):
  if vis[cur]:
    return
  vis[cur] = True

  for nxt in a[cur]:
    if not vis[nxt]:
      parent[nxt] = cur
      dfs(nxt)

dfs(1)

print(*parent[2:], sep='\n')