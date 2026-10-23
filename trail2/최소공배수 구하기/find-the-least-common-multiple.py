n, m = map(int, input().split())

def a(n,m) :
    i=1
    while True :
        
        if i%n ==0 and i%m==0 :
            print(i)
            break
        else :
            i+=1

a(n,m)