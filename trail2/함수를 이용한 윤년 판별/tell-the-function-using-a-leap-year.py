y = int(input())

def findy(y) : 
    if (y % 100 ==0) and (y % 400 != 0) :
        return False
    if y % 4 == 0 :
        return True

    return False

if findy(y) :
    print('true')
else :
    print('false')