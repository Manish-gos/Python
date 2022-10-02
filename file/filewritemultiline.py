#open file for write
f=open("myfile.txt","w")
print("Enter content for file (Type # when you done)")
s=''
while(s!='#'):
    s=input()
    f.write(s+'\n')

f.close()

