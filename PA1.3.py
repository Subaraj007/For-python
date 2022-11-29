n1=input('')
vowels='aeiou'
for i in  n1:
    if i.isalpha():
        if i in vowels:
            print(i,end='')
        elif i.isupper():
            print(i+'o'+i.lower(),end='')
        else:
            print(i+'o'+i,end='')
    else:
        print(i,end='')
if n1[-1] not in '!':
    print('!')
