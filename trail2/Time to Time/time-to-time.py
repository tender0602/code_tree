a, b, c, d = map(int, input().split())

def count(a,b,c,d) :
    return (60*c+d)-(60*a+b)

print(count(a,b,c,d))