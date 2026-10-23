n, m = map(int, input().split())

def fc(n,m) : 
    n_list = []
    m_list = []
    for i in range(1,n//2+1):
        if n % i ==0 :
            n_list.append(i)
    n_list.append(n)

    for j in range(1,m//2+1):
        if m % j ==0 :
            m_list.append(j)
    m_list.append(m)

    for i in range(len(n_list)-1,-1,-1) :
        if n_list[i] in m_list :
            print(n_list[i])
            break


fc(n,m)