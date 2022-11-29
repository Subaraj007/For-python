row=int(input(''))
for i in range(row):
    print('$'*(row-i-1)+'*'*(i+1)+'*'*(i)+'$'*(row-i-1))
for j in range(row-1,0,-1):
    print('$'*(row-j)+'*'*(j)+'*'*(j-1)+'$'*(row-j))

