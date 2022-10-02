a,b=[int(x) for x in input("Enter two numbers").split()]
try:
    f=open("Myfile","w")
    c=a/b
    print(c)
    f.write("We are wirting a value %d"%c)
except ZeroDivisionError:
    print("Please enter a valid number")
    print("Division by zero is not allowed ")
else:
    print("You have entered a non zero number")
finally:
    f.close()
    print("File is closed")
print("Program end!")