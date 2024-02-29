import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = defaultdict(list)
vis = [False] * 1001

for _ in range(m):
  u, v = map(int, input().rstrip().split())
  a[u].append(v)
  a[v].append(u)

def dfs(cur):
  if vis[cur]:
    return
  vis[cur] = True

  for nxt in a[cur]:
    if not vis[nxt]:
      dfs(nxt)

cnt = 0
for i in range(1, n + 1):
  if not vis[i]:
    cnt += 1
    dfs(i)

print(cnt)