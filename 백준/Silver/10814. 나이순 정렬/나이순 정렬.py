import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = []

for i in range(n):
  age, name = input().split()
  a.append([int(age), name])

for a, b in sorted(a, key=lambda x: x[0]):
  print(a, b)