import sys
import math
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
    if a == b: return False
    self.p[a] += self.p[b]
    self.p[b] = a
    return True
  
  def __str__(self):
    return ' '.join(map(str, self.p))

def get_dist(i, j):
  return math.sqrt(pow(a[i][0] - a[j][0], 2) + pow(a[i][1] - a[j][1], 2))

n, m = map(int, input().split())
uf = UnionFind(n + 1) 
a = [[*map(float, input().split())] for _ in range(n)]
e = []

for i in range(n): 
  for j in range(n):
    if i == j: continue
    e.append([get_dist(i, j), i, j])

e.sort()

res = 0
for _ in range(m):
  u, v = map(int, input().split())
  uf.union(u-1, v-1)

for w, u, v in e:
  if uf.union(u, v):
    res += w
print(f'{res:.2f}')