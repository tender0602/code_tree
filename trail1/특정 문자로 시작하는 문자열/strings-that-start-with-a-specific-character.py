n= int(input())
lst = []
answer = []

for i in range(n) :
    lst.append(input())

c=input()

for j in lst :
    if c == j[0] :
        answer.append(len(j))

print(len(answer),end=' ')
print(f'{sum(answer)/len(answer):.2f}')