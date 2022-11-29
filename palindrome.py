def check(s,n):
    if n==1:
        return s[0]
    else:
        return s[n-1]+check(s,n-1)
s=input("enter string: ")
n=len(s)
if s==check(s,n):
    print("palindrome")
else:
    print("non palindrome")
print(check(s,n))
