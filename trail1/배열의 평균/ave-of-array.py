arr = []

for i in range(2):
    arr.append(list(map(int, input().split())))

# 가로 평균
for i in range(2):
    print(f"{sum(arr[i]) / 4:.1f}", end=" ")
print()

# 세로 평균
for j in range(4):
    avg = (arr[0][j] + arr[1][j]) / 2
    print(f"{avg:.1f}", end=" ")
print()

# 전체 평균
total = 0
for i in range(2):
    total += sum(arr[i])

print(f"{total / 8:.1f}")