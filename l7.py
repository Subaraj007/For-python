a=['1','2','3','4']
maxi=a[0]
for i in range(1,len(a)):
	if maxi<a[i]:
		maxi=a[i]
print(maxi)
