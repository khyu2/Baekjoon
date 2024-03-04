import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [0] * (n)
vis = [False] * (n + 1)

def dfs(depth):
  if depth == m:
    for i in range(m): print(a[i], end=' ')
    print()
    return
  
  for i in range(1, n + 1):
    if not vis[i] and a[depth - 1] < i:
      vis[i] = True
      a[depth] = i
      dfs(depth + 1)
      a[depth] = i
      vis[i] = False

dfs(0)