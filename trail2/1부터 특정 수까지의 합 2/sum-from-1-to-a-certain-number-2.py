n = int(input())
def check(n):
    if n == 0 : 
        return 0
    return n+check(n-1)

print(check(n))