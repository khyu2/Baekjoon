import sys
input = lambda: sys.stdin.readline().rstrip()

a = [[*map(int, input().split())] for _ in range(9)]
zero = []

for i in range(9):
  for j in range(9):
    if a[i][j] == 0: zero.append([i, j])

def rows(i, x):
  for j in range(9):
    if x == a[i][j]: return False
  return True

def cols(j, x):
  for i in range(9):
    if x == a[i][j]: return False
  return True

def box(x, y, k):
  for i in range(3):
    for j in range(3):
      if k == a[x // 3 * 3 + i][y // 3 * 3 + j]: return False
  return True

def dfs(cnt):
  if cnt == len(zero):
    print()
    for i in a:
      print(*i)
    exit()

  for i in range(1, 10):
    x, y = zero[cnt][0], zero[cnt][1]
    if rows(x, i) and cols(y, i) and box(x, y, i):
      a[x][y] = i
      dfs(cnt + 1)
      a[x][y] = 0

dfs(0)