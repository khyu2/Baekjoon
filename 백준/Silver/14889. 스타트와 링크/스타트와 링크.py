import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
s = [sum(a[i]) for i in range(n)]
s = sum(s)

ans = 1e10
def dfs(p, idx):
  if len(p) == n // 2:
    tmp = []
    for i in range(1, n + 1):
      if i not in p: tmp.append(i)

    res = 0
    for i, x in enumerate(p):
      for j, y in enumerate(p):
        if i != j: res += a[x-1][y-1]

    res2 = 0
    for i, x in enumerate(tmp):
      for j, y in enumerate(tmp):
        if i != j: res2 += a[x-1][y-1]
    global ans
    if ans > abs(res - res2):
      ans = abs(res - res2)

  else:
    for i in range(idx, n + 1):
      if i not in p:
        p.append(i)
        dfs(p, i)
        p.pop()

dfs([], 1)
print(ans)