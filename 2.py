n=5
for i in range(n):
    for j in range(n-i-1):
        print('$',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    for p in range(i):
        print('*',end=' ')
    for s in range(n-i-1):
        print('$',end=' ')
    print(i[-1])
