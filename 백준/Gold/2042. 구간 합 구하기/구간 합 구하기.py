import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTree:
  def __init__(self, a):
    self.a = a
    self.tree = [0] * (4 * len(a))
    self.build(1, 0, len(a) - 1)

  def build(self, node, s, e):
    if s == e: self.tree[node] = self.a[s]
    else:
      self.build(node*2, s, (s + e) // 2)
      self.build(node*2+1, (s+e)//2+1, e)
      self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
    
  def query(self, node, s, e, l, r): # find [l, r]
    if s > r or e < l: return 0 # not overlap
    if l <= s and e <= r: return self.tree[node] # full overlap
    return self.query(node*2, s, (s+e)//2, l, r) + self.query(node*2+1, (s+e)//2+1, e, l, r)
  
  def update(self, node, s, e, idx, val):
    if s == e: self.a[idx] = self.tree[node] = val
    else:
      if idx <= (s + e) // 2:
        self.update(node*2, s, (s+e)//2, idx, val)
      else:
        self.update(node*2+1, (s+e)//2+1, e, idx, val)
      self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
tree = SegmentTree(a)

for _ in range(m + k):
  cmd, x, y = map(int, input().split())
  if cmd == 1: tree.update(1, 0, n - 1, x - 1, y)
  else: print(tree.query(1, 0, n - 1, x-1, y-1))