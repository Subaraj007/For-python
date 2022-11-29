l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


p=l.find(input(''))
for i in range(p+1):
    print('.'*(p-i)+l[i])
