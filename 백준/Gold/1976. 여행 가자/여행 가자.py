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

  def getSize(self, n):
    return abs(self.p[n])

  def same_set(self, a, b):
    return self.find(a) == self.find(b)
  
  def __str__(self):
    return ' '.join(map(str, self.p))
  
n = int(input())
m = int(input())
uf = UnionFind(n + 1)

for i in range(n):
  for j, x in enumerate(list(map(int, input().split()))):
    if x:
      uf.union(i, j)

# print(uf)
a = list(map(int, input().split()))
for i in range(m - 1):
  if not uf.same_set(a[i]-1, a[i+1]-1):
    print('NO')
    exit()

print('YES')