f=open("C:/files/text.txt","r")
output=open("C:/files/text1.txt","w")
str=f.read()
p=''
for i in range(1,int(str[0])+1):
    for j in range(1,(6-i)):
        output.write=p+" "
    output.write=(str[1:])*i
    

