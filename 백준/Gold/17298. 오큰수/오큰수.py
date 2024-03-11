import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
stack = []
ans = [-1] * n

for i, x in enumerate(a):
  if not stack:
    stack.append([x, i])
  elif stack and x < stack[-1][0]:
    stack.append([x, i])
  else:
    while stack and x > stack[-1][0]:
      ans[stack[-1][1]] = x
      stack.pop()
    
    stack.append([x, i])
  # print('stack = ', stack)
  # print('answer = ', ans)

print(' '.join(map(str, ans)))