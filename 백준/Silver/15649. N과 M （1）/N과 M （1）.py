n, m = map(int, input().split())
vis = [False] * (n + 1)

def dfs(a):
  if len(a) == m:
    print(*a)
    return
  
  for i in range(1, n + 1):
    if not vis[i]:
      vis[i] = True
      a.append(i)
      dfs(a)
      a.pop()
      vis[i] = False

dfs([])