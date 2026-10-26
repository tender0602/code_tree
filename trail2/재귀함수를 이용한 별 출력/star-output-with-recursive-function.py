n = int(input())

def func1(n) :
    if n == 0 :
        return 
    func1(n-1)
    print('*'*n)


func1(n)