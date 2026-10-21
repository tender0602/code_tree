n = int(input())
cnt1 = 0
cnt2 = 0

for i in range(n):
    data = input()
    cnt1 += len(data)
    if 'a' == data[0] :
        cnt2 +=1
print(cnt1, cnt2)