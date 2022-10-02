import re
str="take up one idea.Take a idea once a time"
result = re.search(r'o\w\w',str)
print(result.group())

result = re.findall(r'o\w\w',str)
print(result)

result = re.match(r'T\w\w',str)
print(result.group())

