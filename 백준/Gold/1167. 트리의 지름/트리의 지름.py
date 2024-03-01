import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)
w = 0
idx = 0

def dfs(cur, cost):
  global w
  global idx

  if vis[cur]:
    return
  vis[cur] = True

  if w < cost:
    w = cost
    idx = cur

  for i, ncost in a[cur]:
    if not vis[i]:
      dfs(i, cost + ncost)

for i in range(1, n + 1):
  tmp = list(map(int, input().rstrip().split()))
  j = 1
  while tmp[j] != -1:
    a[tmp[0]].append([tmp[j], tmp[j + 1]])
    j += 2
  
dfs(1, 0)
vis = [False] * (n + 1)
w = 0

dfs(idx, 0)
print(w)

