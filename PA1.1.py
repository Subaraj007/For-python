n=input('').split()
l1=[]
l2=[]
for i in n:
    if i.isalpha():
        l1.append(ord(i))
    else:
        l2.append(i)
mini1=min(l1)
l3=[]
for j in range(len(l1)):
    l3.append(chr(mini1))
    l1.remove(mini1)
mini2=min(l2)
l4=[]
for k in range(lenl2):
    l4.append(chr(mini2))
    l2.remove(mini2)
print(l3,l4)
