n1=list(map(int,input().split()))
f=[]
while len(f)<n1[0]:
    p=list(map(int,input().split()))
    f.append(p)
n2=list(map(int,input().split()))
d=[]
while len(d)<n2[0]:
    s=list(map(int,input().split()))
    d.append(s)
for i in range(len(f)):
    c=''
    for j in range(len(d[0])):
        v=0
        for k in range(len(f[0])):
            v+=f[i][k]*d[k][j]
        c+=str(v)+' '
    print(c)

    
