import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())
cnt = 0

def go(n, row, col):
    global cnt

    if n == 2:
        for i in range(row, row + 2):
            for j in range(col, col + 2):
                if i == r and j == c:
                    return
                cnt += 1
    else:
        n //= 2
        if row <= r < row + n and col <= c < col + n: # 1
            go(n, row, col)
        elif row <= r < row + n and c >= col + n: # 2
            cnt += n * n
            go(n, row, col + n)
        elif r >= row + n and col <= c < col + n: # 3
            cnt += n * n * 2
            go(n, row + n, col)
        else:
            cnt += n * n * 3
            go(n, row + n, col + n)

go(2 ** N, 0, 0)

print(cnt)