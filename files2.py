fh = open(input("Enter file name: "))
count = 0
value = 0
for line in fh:
	line = line.rstrip()
	if not line.startswith("X-DSPAM-Confidence:") : continue
	else :
		count = count+1
		value = value + float(line[line.find(":")+1 :])
print("Average spam confidence:", value/count)