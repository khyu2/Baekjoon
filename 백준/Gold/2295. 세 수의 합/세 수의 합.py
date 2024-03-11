import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(input()) for _ in range(n)]
p = []

def binary_search(l, r, x):
  while l <= r:
    mid = l + (r - l) // 2
    if p[mid] == x: return True
    elif p[mid] > x: r = mid - 1
    else: l = mid + 1
  return False

a.sort()
for i in range(n):
  for j in range(n):
    p.append(a[i] + a[j])

p.sort()
for i in range(n - 1, -1, -1):
  for j in range(n):
    k = a[i] - a[j]
    if binary_search(0, len(p) - 1, k):
      print(a[i])
      exit()
