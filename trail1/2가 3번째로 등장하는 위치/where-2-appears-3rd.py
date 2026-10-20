a = input()
b = list(map(int,input().split()))

cnt=0
index=0
for i in b :
    index+=1
    if i == 2 :
        cnt +=1
    if cnt == 3 :
        print(index)
        break

