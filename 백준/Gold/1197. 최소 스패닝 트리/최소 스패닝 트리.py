import sys
input = lambda: sys.stdin.readline().rstrip()

def find(x):
  if p[x] < 0: return x
  p[x] = find(p[x])
  return p[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a == b: return False
  p[a] += p[b]
  p[b] = a
  return True

n, m = map(int, input().split())
p = [-1] * (n + 1)
e = []

for _ in range(m):
  u, v, w = map(int, input().split())
  e.append([w, u, v])

e.sort()

res = 0
for w, u, v in e:
  if union(u, v): res += w

print(res)