import sys
import math
input = lambda: sys.stdin.readline().rstrip()

n = input()
m = int(input())
broken = list(map(int, input().split())) if m else []
a = [str(i) for i in range(10) if i not in broken]

def func(n, m):
  num = int(n)
  ret = math.inf

  diff = abs(100 - num)
  if diff == 0: return 0

  ret = min(ret, diff)
  for i in range(1000001):
    if all(btn in a for btn in str(i)):
      ret = min(ret, abs(num - i) + len(str(i)))

  return ret

print(func(n, m))
