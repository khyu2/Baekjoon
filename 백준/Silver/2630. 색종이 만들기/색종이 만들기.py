import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = []
blue = 0
white = 0

for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))

def check(n, x, y): # n : 현재 판 크기, x, y : 시작 좌표
    color = a[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if a[i][j] != color:
                return False
    return True

def go(n, x, y):
    global blue
    global white

    if n == 1: # 더 이상 쪼갤 수 없다면 현재 색에 따라 count++
        if a[x][y] == 1:
            blue += 1
        else:
            white += 1
    else: # 쪼갤 수 있고
        if check(n, x, y): # 모든 색이 같다면
            if a[x][y]: # 색에 따라 +1
                blue += 1
            else:
                white += 1
        else: # 색이 다르면
            n //= 2
            go(n, x, y)
            go(n, x, y + n)
            go(n, x + n, y)
            go(n, x + n, y + n)

go(n, 0, 0)
print(white, blue, sep='\n')

