n = int(input())
a = [*map(int, input().split())]
d = [-1 for _ in range(n)]

d[0] = a[0]
for i in range(1, n):
  d[i] = max(d[i-1] + a[i], a[i])

print(max(d))