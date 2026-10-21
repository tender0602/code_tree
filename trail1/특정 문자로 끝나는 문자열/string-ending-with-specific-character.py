lst = []
for i in range(10) :
    lst.append(input())
a=input()
cnt=0
for j in lst :
    if j[-1] == a :
        print(j)
        cnt+=1
        
if cnt == 0:
    print('None')
    