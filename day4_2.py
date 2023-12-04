from collections import deque
f = open("input_day4.txt","r")
output = 0
queue = deque()
for line in f:
	cards = 1
	if len(queue) != 0:
		cards = queue.popleft() + 1
	output = output + cards
	tmp = line.split(": ")
	tmp_nums = tmp[1].split("|")
	winning_nums = tmp_nums[0].split()
	card_nums = tmp_nums[1].split()
	count = sum(num in card_nums for num in winning_nums)
	for i in range(count):
		if i < len(queue):
			queue[i] = queue[i] + cards
		else:
			queue.append(cards)
print(output)