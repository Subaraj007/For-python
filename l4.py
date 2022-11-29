n=ord(input(''))
p=n-65
for i in range(p):
    for j in range(p+1):
        print('*'*(p-j)+chr(65+j)+chr(64+j)+'*'*(p-j))
    for k in range(p-1,0,-1):
        print('*'*(p-k)+chr(65+k)+chr(65+p-k)+'*'*(p-k))
        

