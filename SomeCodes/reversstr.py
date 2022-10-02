s=input("Enter a string")
s=s[::-1]
print(s)
result=""
i=len(s)-1
while i>=0:
    result=result+s[i]
    i-=1
print(result)

#using join method
print(''.join(reversed(s)))