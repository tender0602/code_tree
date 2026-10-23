n = int(input())
def aa(n) : 
    if (n %2) ==0 and (sum(map(int,list(str(n)))) % 5 == 0) :
        answer = "Yes"
    else :
        answer = "No"
    return answer
print(aa(n))

# Please write your code here.