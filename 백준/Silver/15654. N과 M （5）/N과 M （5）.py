import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for i in permutations(a, m):
  print(*i)