import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

res = 0
for i in reversed(a):
  if k // i > 0:
    res += k // i
    k %= i

print(res)