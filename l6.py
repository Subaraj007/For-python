n=input('')


if 1<=int(n)<=100000 or len(n)==1:
    for i in range(1,len(n)//2+1):
        
        if n[i-1]==n[-i]:
            
            
            print(n[-i])
            print(n[i-1])

    print('yes')
else:
    print('no')
