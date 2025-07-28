import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(int(input())):
    a = [*map(int, input().split())]
    cnt = 0
    for i in range(1, 21):
        for j in range(1, i):
            if a[j] > a[i]:
                tmp = a[i]
                for k in range(i, j, -1):
                    a[k] = a[k - 1]
                    cnt += 1
                a[j] = tmp
                break

    print(a[0], cnt)