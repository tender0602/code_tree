text = input()
pattern = input()

def check(text,pattern)  :
    if pattern in text :
        id=text.index(pattern)
        return id
    else :
        return -1
    
print(check(text,pattern))