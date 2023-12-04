import re

output = 0
f = open("input_day1.txt","r")
for line in f:
	digits = ''.join(i for i in line if i.isdigit())
	first_digit = int(digits[0])
	last_digit = int(digits[-1])
	output = output + first_digit * 10 + last_digit

print(output)