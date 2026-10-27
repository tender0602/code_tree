n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

answer = []
for i in str :
    if t in i and i.index(t)==0:
        answer.append(i)

answer.sort()
print(answer[k-1])

