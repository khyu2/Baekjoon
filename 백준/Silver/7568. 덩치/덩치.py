import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
b = [1 for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == j: continue
    if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
      b[i] += 1
    
print(*b)