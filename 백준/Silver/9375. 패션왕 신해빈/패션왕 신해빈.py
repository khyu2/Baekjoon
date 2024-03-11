import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
  n = int(input())
  a = {}

  for _ in range(n):
    x, y = input().split()
    if y not in a: a[y] = 1
    else: a[y] += 1

  ans = 1
  for key, val in a.items(): 
    ans *= val + 1
  
  print(ans - 1)