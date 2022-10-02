s="You are awesome"
print(s)

s1="""You are awesome,
And you are very cool
person"""
print(s1)

#indexing return->u
print(s[2])

#repeat string-> You are awesome You are awesome
print(s*2)

#string length
print(len(s))

#slicing
""" op ->
You are 
You are 
You are awesome
om"""
print(s[0:8])
print(s[:8])
print(s[0:])
print(s[-3:-1])

#steping in sliceing
'''Yuaea
emosewa era uoY
emosewa era uoY'''
print(s[0:10:2])
print(s[15::-1]) #reverse string
print(s[::-1])   #reverse string

#strip spaces
str="      remove spaces           "
print(str)
print(str.strip())
print(str.lstrip())
print(str.rstrip())

#find
print(s.find("aw"))
print(s.find("aw",0,15))
print(s.find("aw",0,5))

#count
print(s.count("a"))

#upper,lower,title
print(s.upper())
print(s.lower())
print(s.title())


