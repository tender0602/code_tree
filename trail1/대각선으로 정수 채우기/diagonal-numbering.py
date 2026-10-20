n, m = map(int, input().split())

matrix = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

for i in range(n + m - 1):
    c = i
    b = 0

    while c >= 0:
        if b < n and c < m:
            matrix[b][c] = cnt
            cnt += 1

        b += 1
        c -= 1

for i in matrix:
    print(*i)