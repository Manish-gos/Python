str=input("Enter string")
result=[]
for i in str:
    if i not in result:
        result.append(i)

str=''.join(result)
print(str)