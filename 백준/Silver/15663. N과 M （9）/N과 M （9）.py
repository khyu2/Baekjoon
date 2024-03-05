import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))
vis = [False] * (n + 1)
s = set()

a.sort()

def dfs(out, depth):
  if depth == m:
    s.add(tuple(out))
  
  for i in range(n):
    if not vis[i]:
      vis[i] = True
      out.append(a[i])
      dfs(out, depth + 1)
      out.pop()
      vis[i] = False

dfs([], 0)

answer = []
for i in s:
  tmp = []
  for j in i:
    tmp.append(j)
  answer.append(tmp)

answer.sort()

for i in answer:
  print(*i)