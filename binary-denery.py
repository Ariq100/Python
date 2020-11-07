binery = list(input("Input a binary number: "))
value = 0

for i in range(len(binery)):
	digit = binery.pop()
	if digit == '1':
		value = value + pow(2, i)
print("the denery value is : ", value)

