fh = open(input("Enter file name: "))
count = dict()
for line in fh:
	line = line.split()
	if len(line) >= 6 and line[0] == "From":
		time = line[5].split(":")
		count[time[0]] = count.get(time[0],0)+1
for h,v in sorted([(h,v) for h,v in count.items()]) : print(h,v)