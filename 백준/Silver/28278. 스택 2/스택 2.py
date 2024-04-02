import sys
input = lambda: sys.stdin.readline().rstrip()

st = []
for i in range(int(input())):
  op, *a = input().split()
  op = int(op)
  if op == 1: st.append(int(a[0]))
  elif op == 2: print(-1 if not st else st.pop())
  elif op == 3: print(len(st))
  elif op == 4: print(1 if not st else 0)
  else: print(-1 if not st else st[-1])