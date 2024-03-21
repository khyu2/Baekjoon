import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = []
for cap in [*map(int, input().split())]:
  a.append([False, cap])

def rotate(a):
  return [a.pop()] + a[:]

cnt = 0
while True:
  cnt += 1

  a = rotate(a) # 벨트 회전

  if a[n-1][0]: # 내리는 위치에 있는 로봇 내리기
    a[n-1][0] = False

  for i in range(len(a) - 2, -1, -1):
    onRobot, cap = a[i]

    if onRobot and not a[i+1][0] and a[i+1][1] > 0: # 현재 로봇이고, 옆 칸에 로봇이 없고, 옆 칸 내구도가 1 이상이라면
      a[i+1][1] -= 1
      a[i][0] = False
      a[i+1][0] = True

  if a[n-1][0]: # 내리는 위치에 있는 로봇 내리기
    a[n-1][0] = False
    
  if a[0][1] > 0: # 올리는 위치에 로봇 올리기 
    a[0][0] = True
    a[0][1] -= 1

  # print(a)
  zero = 0
  for r, c in a:
    if c < 1: zero += 1
  if zero >= k: break

print(cnt)