import re

fh = open(input("Enter file name: "))
num = re.findall('[0-9]+' , fh.read())
for i in range(len(num)) : num[i] = int(num[i])
print(sum(num))
