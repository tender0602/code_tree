n = int(input())

def a(n) :
    k=1
    for i in range(n) :
        for j in range(n-1):
            if k%9==0:
                print(9,end=' ')
            else :
                print(k%9,end=' ')
            k+=1
        if k%9 == 0 :
            print(9)
        else :
            print(k%9)
        k+=1
a(n)
