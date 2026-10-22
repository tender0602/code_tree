A= input()
cnt_ee=0
cnt_eb=0
for i in range(0,len(A)-1) :
    if 'ee' == A[i:i+2] :
        cnt_ee+=1
for i in range(0,len(A)-1) :
    if 'eb' == A[i:i+2] :
        cnt_eb+=1

print(cnt_ee,cnt_eb)
