a, b = map(int, input().split())

def on(a,b) :
    cnt=0
    for i in range(a,b+1):
        if i% 2==0 :
            continue
        if int(list(str(i))[-1])==5 :
            continue
        if i % 3==0 and i % 9 != 0 :
            continue
        cnt+=1
    return cnt

print(on(a,b))
# Please write your code here.