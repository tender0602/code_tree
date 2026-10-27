n = int(input())
arr = list(map(int, input().split()))
answer = []
for i in arr :
    answer.append(i)
    if len(answer) %2 !=0 :
        sort_list = sorted(answer)
        print(sort_list[(len(sort_list)//2)],end=' ')

