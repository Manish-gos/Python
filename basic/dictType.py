dic1={1:"Manish",2:"Goswami",3:"Akash",4:"Patil"}
print(dic1)
print(dic1.items())
k=dic1.keys()
for i in k:
    print(i)
v=dic1.values()
for i in v:
    print(i)
print(dic1[2])
del dic1[3]
print(dic1)
