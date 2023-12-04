import re

def get_indices(n):
	output = []
	output.append(("one", "o1e"))
	output.append(("two", "t2o"))
	output.append(("three", "t3e"))
	output.append(("four", "f4r"))
	output.append(("five", "f5e"))
	output.append(("six", "s6x"))
	output.append(("seven", "s7n"))
	output.append(("eight", "e8t"))
	output.append(("nine", "n9e"))
	return output

def replace_numbers(n):

	tups = get_indices(n)

	for tup in tups:
		n = n.replace(tup[0], tup[1])

	return n

cur = 1
output = 0
f = open("input_day1.txt","r")
for line in f:
	line2 = replace_numbers(line.rstrip())
	digits = ''.join(i for i in line2 if i.isdigit())
	first_digit = int(digits[0])
	last_digit = int(digits[-1])
	print("Line #" + str(cur) + ": " + line.rstrip() + " " + line2 + " " + str(first_digit*10 + last_digit))
	output = output + first_digit * 10 + last_digit
	cur = cur+1

print(output)