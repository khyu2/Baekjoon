import sys
input = lambda: sys.stdin.readline().rstrip()

ans = 0
n = int(input())
vis = [-1] * n

def placeQueen(row):
  for i in range(row):
    if vis[row] == vis[i] or abs(vis[row] - vis[i]) == abs(row - i): return False
  return True

def dfs(cnt):
  global ans
  if cnt == n:
    ans += 1
    return
  
  for i in range(n):
    if vis[cnt] == -1:
      vis[cnt] = i
      if placeQueen(cnt): dfs(cnt + 1)
      vis[cnt] = -1

dfs(0)

print(ans)