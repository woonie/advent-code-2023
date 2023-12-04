import re
f = open("input_day3.txt","r")
def hit(pos,box):
    return box[2] >= pos[0] >= box[0] and box[3] >= pos[1] >= box[1]
symbol_arr = []
num_arr = []
line_num = 0
for line in f:
	for match in re.finditer(r'[\*]', line.strip()):
		symbol_arr.append((line_num,match.start()))
	for match in re.finditer(r'\d+', line.strip()):
		num_arr.append((int(match.group()),(max(0, line_num-1),max(0,match.start()-1), line_num+1, match.end())))
	line_num = line_num+1

output_dict = {}
for num_coord in num_arr:
	num = num_coord[0]
	num_box = num_coord[1]
	for sym_coord in symbol_arr:
		if hit(sym_coord,num_box):
			if sym_coord not in output_dict:
				sym_num_arr = []
			else:
				sym_num_arr = output_dict.get(sym_coord)
			sym_num_arr.append(num)
			output_dict[sym_coord] = sym_num_arr

output = 0
for coord in output_dict:
	num_arr = output_dict.get(coord)
	if len(num_arr) == 2:
		tmp_output = 1
		for num in num_arr:
			tmp_output = tmp_output * num
		output = output + tmp_output
print(output)
