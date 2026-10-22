A = list(input())
while True : 
    if len(A) == 1:
        break
    b=int(input())
    if b >= len(A) :
        A.pop(-1)
    else :
        A.pop(b)
    print(''.join(A))
   
