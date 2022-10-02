# you are good-> good are you
str=input("Enter a string").split(' ')
result=''
i=len(str)-1
while i>=0:
    result=result+str[i]+" "
    i-=1
print(result)


