import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(input()) for _ in range(n)]
st = []
area = 0

a.append(0)
for i in range(n + 1):
  while st and a[i] < a[st[-1]]:
    top = a[st.pop()]
    base = i if not st else i - st[-1] - 1 # *
    area = max(area, top * base)
  st.append(i)

print(area)