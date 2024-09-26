import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, w, l = map(int, input().split())
a = [*map(int, input().split())]
q = deque()

truck_cnt = 0
q_w = 0
done = 0
time = 0

while done < n:
  if truck_cnt < n and len(q) <= w and (not len(q) or q_w + a[truck_cnt] <= l):
    q.append([a[truck_cnt], 0])
    q_w += a[truck_cnt]
    truck_cnt += 1

  # print('올릴 수 있으면 올림', q, q_w, truck_cnt)

  for truck in q: truck[1] += 1

  # print('전진', q)

  if q[0][1] >= w + 1:
    q_w -= q[0][0]
    q.popleft()
    done += 1

  # print('내릴수있으면 내림', q, q_w, truck_cnt)

  if truck_cnt < n and len(q) <= w and (not len(q) or q_w + a[truck_cnt] <= l):
    q.append([a[truck_cnt], 1])
    q_w += a[truck_cnt]
    truck_cnt += 1
  
  # print('올릴수있으면 올림(한칸 전진상태)', q, q_w, truck_cnt)

  time += 1
  # print(q)
  
print(time)