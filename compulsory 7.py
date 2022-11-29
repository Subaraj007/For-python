f=open("C:/files/text.txt","r")
str=f.read()
for i in range(1,int(str[0])+1):
    for j in range(1,(6-i)):
        print(" ",end='')
    print((str[1:])*i)

