str=input("Enter string")
result={}
for i in str:
    if i in result:
        result[i]=result.get(i,0)+1
    else:result[i]=1
for k,v in result.items():
    print( k,v)