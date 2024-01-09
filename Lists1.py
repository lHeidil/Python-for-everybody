fh = open(input("Enter file name: "))
lst = list()
for line in fh :
	line = line.rstrip()
	line = line.split()
	for word in line :
		if not word in lst : lst.append(word)
lst.sort()
print(lst)