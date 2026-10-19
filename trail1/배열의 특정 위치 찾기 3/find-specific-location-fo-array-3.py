arr = list(map(int,input().split()))
for i in range(len(arr)) :
    if arr[i] == 0 :
      answer = arr[i-3]+arr[i-2]+arr[i-1]
      break
print(answer)