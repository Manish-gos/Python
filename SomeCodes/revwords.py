# you are good-> uoy era doog
str=input("Enter a string").split(' ')
result=''
for i in str:
    result=result+''.join(reversed(i))+" "

print(result)


