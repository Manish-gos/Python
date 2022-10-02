a=[1,2,3,4,5]
b=[5,4,2,8,9]
z=[]
k=[]
for i in a:
    if i in b:
     z.append(i)

print(z)
k=[x for x in a if x in b]
print(k)
