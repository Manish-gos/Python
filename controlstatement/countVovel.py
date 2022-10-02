word=input("Enter a word")
vovel={'a','e','i','o','u'}
r={}
for c in word:
    if c in vovel:
        r[c]=r.get(c,0)+1

for k, v in sorted(r.items()):
    print(k , "is present ",v,"times")

