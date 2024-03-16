import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(input()) for _ in range(n)]

def sort(a):
  n = len(a)

  for i in range(n):
    for j in range(i + 1):
      if a[i] < a[j]:
        a[i], a[j] = a[j], a[i]

sort(a)

print(*a, sep='\n')