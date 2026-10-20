n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q) :
    query = list(map(int, input().split()))
    if query[0] == 1 :
        a = query[1]
        print(arr[a-1])
    elif query[0] == 2 :
        b = query[1]
        if b not in arr :
            print(0)
        else :
            print(arr.index(b)+1)
    else :
        s,e = query[1], query[2]
        print(*arr[s-1:e])

    

