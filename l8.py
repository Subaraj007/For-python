l=[]
n=input('').split()
print(n)
for i in n:
    k=eval(i)
    l.append(k)
s=l[0]
for k in l:
    if s>k:
        s=k
print('mini',s)
