import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = list(range(1, n + 1))

for i in list(permutations(a, m)):
  print(' '.join(map(str, i)))