import sys,os

if os.path.isfile("myfile.txt"):
    f=open("myfile.txt","r")
    print(f.read())
    f.close()
else:
    print("file does not exist")
    sys.exit()

