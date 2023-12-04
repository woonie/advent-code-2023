f = open("input_day2.txt","r")
output = 0
for line in f:
	output_cur = 1
	color_dict = {}
	tmp = line.split(": ")
	cur = int(tmp[0].split()[1])
	games = tmp[1].split("; ")
	for game in games:
		colors = game.split(", ")
		for color_num in colors:
			color_arr = color_num.split()
			color_amt = int(color_arr[0])
			color = color_arr[1]
			if color not in color_dict:
				color_dict[color] = color_amt
			else:
				if color_amt > color_dict.get(color):
					color_dict[color] = color_amt
	for color_key in color_dict:
		output_cur = output_cur * color_dict[color_key]
	output = output + output_cur
print(output)