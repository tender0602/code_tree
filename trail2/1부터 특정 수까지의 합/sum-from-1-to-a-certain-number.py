n = int(input())

def a(n) :
    sum=0
    
    for i in range(n+1) :
        sum+=i
    return sum//10

answer = a(n)
print(answer)

    
