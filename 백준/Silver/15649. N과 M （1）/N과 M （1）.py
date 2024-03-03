import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = []
vis = [False] * (n + 1)

def dfs(depth):
  if depth == m:
    print(*a)
    return
  
  for i in range(1, n + 1):
    if not vis[i]:
      vis[i] = True
      a.append(i)
      dfs(depth + 1)
      a.pop()
      vis[i] = False

dfs(0)