string = input("entre string: ")
for i in string:
	if i.isupper(): i = i.lower()
	else: i = i.upper()
	print(i , end ="")