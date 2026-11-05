
from itertools import product

K, N = map(int, input().split())

for seq in product(range(1, K + 1), repeat=N):
    print(*seq)
