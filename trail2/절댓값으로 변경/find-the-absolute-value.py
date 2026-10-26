n = int(input())
arr = list(map(int, input().split()))

def ab(arr) :
    for i in range(n) :
        arr[i] = abs(arr[i])
    return arr

print(*ab(arr))
