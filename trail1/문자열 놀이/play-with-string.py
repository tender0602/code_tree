lst = list(map(str,input().split()))
S=list(str(lst[0]))
n= int(lst[1])
for i in range(n) :
    q=input().split()
    if q[0] == '1':
        q = list(map(int,q))
        S[q[1]-1],S[q[2]-1] = S[q[2]-1],S[q[1]-1]
        print(''.join(S))
    elif q[0] == '2' :
        for i in range(len(S)) :
            if S[i] == q[1] :
                S[i] = q[2]
        print(''.join(S))
