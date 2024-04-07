import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]

res = 0
def go(cur, val):
  if cur >= n:
    global res
    # print('check', cur, val)
    res = max(res, val)
    return
  
  if cur + a[cur][0] <= n: go(cur + a[cur][0], val + a[cur][1])
  go(cur + 1, val)

go(0, 0)
print(res)
  