lst=eval(input("Enter a list: "))
print(lst)
l2=[]
for i in lst:
    if i not in l2:
        l2.append(i)
print(l2)

s=set(lst)
print(s)