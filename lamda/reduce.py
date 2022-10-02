from functools import reduce

lst=[2,4,3,7,6,8,9,1]
f=reduce(lambda x,y:x+y,lst)
print(f)