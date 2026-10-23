a, o, c = input().split()
a = int(a)
c = int(c)

def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def multi(a, c):
    return a * c

def div(a, c):
    return a // c

if o == '+':
    result = plus(a, c)

elif o == '-':
    result = minus(a, c)

elif o == '*':
    result = multi(a, c)

elif o == '/':
    result = div(a, c)

else:
    result = False

if result == False :
    print(False)
else :
    print(f'{a} {o} {c} = {result}')