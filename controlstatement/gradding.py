py=int(input("Physics"))
ch=int(input("Chemistry"))
math=int(input("Maths"))
if py>=35 and ch>=35 and math >=35:
    avg=(math+py+ch)/3
    if avg<=59:print("Your grade is C")
    elif avg>=60 and avg<= 69: print("Your grade is B")
    else:print("Your grade is A")
else:print("You are Failed")