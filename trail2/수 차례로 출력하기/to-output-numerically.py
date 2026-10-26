n = int(input())

def check1(n):
    if n == 0 :
        return 
    print(n,end=' ')
    check1(n-1)
def check2(n):
    if n == 0 :
        return 
    check2(n-1)
    print(n,end=' ')
    
check2(n)
print()
check1(n)