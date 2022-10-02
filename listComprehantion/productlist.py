a=[1,2,3,4,5]
b=[5,6,7,8,9]
z=[]
k=[]
for i in range(len(a)):
    z.append(a[i]*b[i])

print(z)
k=[a[x]*b[x] for x in range(len(a))]
print(k)
