def numerodepasos(n):
    l=[]
    t=[]
    if n%2==0:
        contador=int(n/2+1)
        for i in range(1,contador):
            t.append(i)
            t.append(n-i*2)
            l.append(t)
            t=[]
    else:
        contador=int((n+1)/2)
        for i in range(1,contador):
            t.append(i)
            t.append(n-i*2)
            l.append(t)
            t=[]
        
    print(l)
        
        
numerodepasos(11)