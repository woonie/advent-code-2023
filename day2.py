f = open("input_day2.txt","r")
output = 0
max_dict = {'red': 12, 'green': 13, 'blue': 14}
for line in f:
	tmp = line.split(": ")
	cur = int(tmp[0].split()[1])
	games = tmp[1].split("; ")
	for game in games:
		colors = game.split(", ")
		for color_num in colors:
			color_arr = color_num.split()
			color_amt = int(color_arr[0])
			color = color_arr[1]
			if color_amt > max_dict.get(color):
				cur = 0
	output = output + cur

print(output)