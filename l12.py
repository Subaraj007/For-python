n=input('')
l=[]
a=int()
k=[]
for i in n:
    if i.islower() and n.isalpha():
        a=ord(i)
        l.append(a)
        print(l)
if l.sort()==l:
    print('order')
elif l==l[-1::-1]:
    print('reverse')
else:
    print('not order')
