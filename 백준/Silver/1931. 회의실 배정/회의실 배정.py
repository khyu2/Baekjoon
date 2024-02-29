import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = [tuple(map(int, input().rstrip().split())) for i in range(n)]

a.sort(key = lambda x : (x[1], x[0]))

end = a[0][1]
cnt = 1
for i in range(1, n):
    if end <= a[i][0]:
        # print(end, a[i][0])
        cnt += 1
        end = a[i][1]

print(cnt)