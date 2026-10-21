a= input()
b=input()
c= input()
lst=[a,b,c]
length=[len(a),len(b),len(c)]
max_len=max(length)
min_len=min(length)
answer = abs(max_len - min_len)
print(answer)