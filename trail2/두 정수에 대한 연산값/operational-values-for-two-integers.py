a, b = map(int, input().split())

def func1(a,b):
    if a>b :
        a+=25
        b*=2
    else :
        b+=25
        a*=2
    return a, b
print(*func1(a,b))

    