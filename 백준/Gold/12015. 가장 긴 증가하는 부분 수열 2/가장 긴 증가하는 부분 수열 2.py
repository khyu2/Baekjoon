import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [*map(int, input().split())]
lis = [a[0]]

for i in a[1:]:
  if i > lis[-1]:
    lis.append(i)
  else:
    lis[bisect.bisect_left(lis, i)] = i
  
print(len(lis))