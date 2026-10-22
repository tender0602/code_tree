a=input()
b=''.join(list(map(str,input().split())))
for i in range((len(b)//5)+1) :
    print(b[5*i:5*i+5])
    