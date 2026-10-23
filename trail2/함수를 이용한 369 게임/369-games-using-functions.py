a, b = map(int, input().split())

def aa(a,b) : 
    cnt= 0
    for i in range(a,b+1,1) :
        if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)) or (i % 3 == 0) :
            cnt +=1
    
    return cnt

print(aa(a,b))