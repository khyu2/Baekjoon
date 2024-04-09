import sys
import math
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [*map(int, input().split())]
p, q = map(int, input().split())

count = 0
for i in range(n):
  a[i] -= p
  count += 1
  if a[i] > 0: count += int(math.ceil(a[i] / q))
print(count)
    