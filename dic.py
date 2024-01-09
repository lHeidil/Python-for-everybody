fh = open(input("Enter file name: "))
count = dict()
for line in fh:
	line = line.split()
	if len(line) >= 3 and line[0] == "From":
		count[line[1]] = count.get(line[1],0)+1
bigv = None
bigk = None
for k,v in count.items():
	if bigv == None or v > bigv:
		bigk = k
		bigv = v
	else: continue
print(bigk , bigv)