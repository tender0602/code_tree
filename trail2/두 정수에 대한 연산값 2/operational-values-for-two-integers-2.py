a, b = map(int, input().split())

def func1(a,b) :
    if a<b :
        a+=10
        b*=2
    else :
        b+=10
        a*=2

    return a,b

print(*func1(a,b))