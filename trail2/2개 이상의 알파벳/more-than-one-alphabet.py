A = input()

def check(A) :
    lst = []
    answer = 'No'
    for i in A :
        if i not in lst :
            lst.append(i)
    
    if len(lst) >= 2 :
        answer = "Yes"
    
    return answer
print(check(A))
