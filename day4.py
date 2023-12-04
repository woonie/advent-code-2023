f = open("input_day4.txt","r")
output = 0
for line in f:
	tmp = line.split(": ")
	tmp_nums = tmp[1].split("|")
	winning_nums = tmp_nums[0].split()
	card_nums = tmp_nums[1].split()
	count = sum(num in card_nums for num in winning_nums)
	if count > 0:
		output = output + pow(2,count-1)
print(output)