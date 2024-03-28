import bisect
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [*map(int, input().split())]
m = int(input())
query = [*map(int, input().split())]

a.sort()
for i in query:
  print(bisect.bisect_right(a, i) - bisect.bisect_left(a, i), end=' ')