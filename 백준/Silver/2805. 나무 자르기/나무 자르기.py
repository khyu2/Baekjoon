import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = 1; e = max(a)
ans = 0
while s <= e:
  mid = s + (e - s) // 2

  cnt = 0
  for i in a:
    if i - mid > 0: cnt += i - mid

  # print(s, e, mid, cnt)
  if cnt >= m:
    ans = mid
    s = mid + 1
  elif cnt == m:
    ans = mid
    break
  else: e = mid - 1

print(ans)
