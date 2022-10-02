n=int(input("Enter the number of rows"))
str = ' *'
for i in range(1,n+1):
    print(' '*(n-i),end="")
    print(str*i)