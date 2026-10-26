n, m = map(int, input().split())
A = list(map(int, input().split()))


def check(n,m,A) :
    sum=0
    while m != 1:
        sum += A[m-1]
        if m%2 !=0 :
            m-=1
        else :
            m//=2
    sum += A[m-1]

    
    return sum

print(check(n,m,A))
        