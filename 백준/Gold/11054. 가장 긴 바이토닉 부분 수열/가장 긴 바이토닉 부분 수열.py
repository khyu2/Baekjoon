import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [*map(int, input().split())]
inc = [0 for _ in range(n)]
dec = [0 for _ in range(n)]

for i in range(n):
  inc[i] = 1
  for j in range(i):
    if a[i] > a[j] and inc[i] < inc[j] + 1:
      inc[i] = inc[j] + 1

a.reverse()
for i in range(n):
  dec[i] = 1
  for j in range(i):
    if a[i] > a[j] and dec[i] < dec[j] + 1:
      dec[i] = dec[j] + 1
      

dec.reverse()
print(max(map(sum, zip(inc, dec))) - 1)