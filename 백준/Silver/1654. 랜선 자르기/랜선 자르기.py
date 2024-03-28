import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

l, r = 1, max(a)
ans = 0
while l <= r:
  mid = l + (r - l) // 2

  cnt = 0
  for i in a:
    cnt += i // mid
  
  if cnt >= k:
    l = mid + 1
    ans = mid
  else: r = mid - 1

print(ans)
