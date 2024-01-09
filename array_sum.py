size = int(input("entre size: "))
ar = input("enter numbers: ")
ar = ar.split()
ar = [int(i) for i in ar]
output = sum(ar)
print(output)