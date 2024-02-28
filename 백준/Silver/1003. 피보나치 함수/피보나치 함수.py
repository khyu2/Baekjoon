import sys
input = sys.stdin.readline

a = [[0 for _ in range(2)] for _ in range(41)]
a[0][0] = a[1][1] = 1

for i in range(2, 41):
    a[i][0] = a[i-1][0] + a[i-2][0]
    a[i][1] = a[i-1][1] + a[i-2][1]

for _ in range(int(input().rstrip())):
    x = int(input().rstrip())
    print(a[x][0], a[x][1])