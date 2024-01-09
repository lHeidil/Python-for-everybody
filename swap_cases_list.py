string = input("entre string: ")
string = list(string)
for i in range(len(string)):
	if (string[i].isupper()) == True:
		string[i] = string[i].lower()
	else: string[i] = string[i].upper()
print(string)