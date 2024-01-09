count = 0
tot = 0
while True:
	num = input("Enter a number: ")
	if num == "done": break
	try:
		num = float(num)
		tot = tot + num
		count = count + 1
	except: print("Invalid input")
print(tot ,count , (tot/count))
