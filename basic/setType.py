
set={1,1,2,3,4,"man",12.4}
print(type(set))
#print(set.count(1)) these operations are  not allowed on set
#print(set*3)
#print(set[2:5])
#print(set.index("man"))

set.update([22,333])
set.remove(1);
print(set)

f=frozenset(set)
print(f)
#f.update([2,3])
#f.remove(2) not applicable
