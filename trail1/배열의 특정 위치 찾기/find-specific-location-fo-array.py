arr = list(map(int,input().split()))
lst1 = []
lst2 = []
for i in range(1,len(arr),2) :
    lst1.append(arr[i])
for i in range(2,len(arr),3) :
    lst2.append(arr[i])

print(sum(lst1),round(sum(lst2)/len(lst2),1))
