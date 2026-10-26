A = input()


def check(A) :
    answer='No'
    pali = A[::-1]
    if A == pali :
        answer = 'Yes'
    return answer
print(check(A))