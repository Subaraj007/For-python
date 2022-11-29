n1=input('n1= ')
n2=input('n2= ')
n3=input('n3= ')
a=int()
if (n1 in n3) or (n2 in n3):
    print('NOT A SHUFFLE')
   
else:
   
    for i in n1:
        if i in n3:
            a=1
        else:
            break
    for j in n2:
        if j in n3:
            a=1
        else:
            break
if a==1:
    print('SHUFFLE')
    
