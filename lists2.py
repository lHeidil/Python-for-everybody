fh = open(input("Enter file name: "))
count = 0
for line in fh:
	line = line.split()
	if len(line) >= 2 and line[0] == "From":
		print(line[1])
		count = count + 1
	continue
print("There were", count, "lines in the file with From as the first word")
