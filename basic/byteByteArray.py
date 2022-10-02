lst=[2,4,6,234]
b=bytes(lst)
#b=[31] not allowed
print(type(b))
b1=bytearray(lst)
print(type(b1))
b1=[43]