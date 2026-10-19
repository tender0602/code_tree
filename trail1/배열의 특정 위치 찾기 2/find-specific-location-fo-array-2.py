arr = list(map(int,input().split()))

even = 0
odd =0
for i in range(0,len(arr),2) :
    even+=arr[i]
    odd+=arr[i+1]
print(abs(even-odd))