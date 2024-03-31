import sys
input = lambda: sys.stdin.readline().rstrip()

count = 0

def merge_sort(a):
  n = len(a)

  if n == 1: return a
  l = merge_sort(a[:n // 2])
  r = merge_sort(a[n // 2:])
  return merge(l, r)

def merge(l, r):
  global count
  i, j = 0, 0
  res = []
  mid = (len(l) + len(r)) // 2

  while i < len(l) and j < len(r):
    if l[i] <= r[j]:
      res.append(l[i])
      i += 1
    else:
      count += mid - i
      res.append(r[j])
      j += 1
  
  res.extend(l[i:])
  res.extend(r[j:])
  return res

n = int(input())
a = [*map(int, input().split())]
merge_sort(a)

print(count)