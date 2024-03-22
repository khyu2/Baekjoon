import sys
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
  def __init__(self, n):
    self.p = [-1] * n

  def find(self, n):
    if self.p[n] < 0: return n
    self.p[n] = self.find(self.p[n])
    return self.p[n]

  def union(self, a, b):
    a = self.find(a)
    b = self.find(b)
    if a == b: return
    self.p[a] += self.p[b]
    self.p[b] = a

  def __str__(self):
    return ' '.join(map(str, self.p))

n, m = map(int, input().split())
a = [*map(int, input().split())]
store = [[*map(int, input().split())] for _ in range(m)]
uf = UnionFind(n + 1)

for i in range(m):
  p = store[i]
  if p[0] <= 1: continue
  for j in range(1, p[0]):
    uf.union(p[j], p[j + 1])

# print(uf)
count = 0
for i in range(m):
  p = store[i]
  br = False
  for j in range(1, p[0] + 1):
    for x in a[1:]:
      if uf.find(x) == uf.find(p[j]):
        count += 1
        br = True
        break
    if br: break

print(m - count)
      