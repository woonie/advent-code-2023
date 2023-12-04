import re
f = open("input_day3.txt","r")
def hit(pos,box):
    return box[2] >= pos[0] >= box[0] and box[3] >= pos[1] >= box[1]
symbol_arr = []
num_arr = []
line_num = 0
for line in f:
	for match in re.finditer(r'[^A-Za-z0-9\.]', line.strip()):
		symbol_arr.append((line_num,match.start()))
	for match in re.finditer(r'\d+', line.strip()):
		num_arr.append((int(match.group()),(max(0, line_num-1),max(0,match.start()-1), line_num+1, match.end())))
	line_num = line_num+1

output = 0
for num_coord in num_arr:
	num = num_coord[0]
	num_box = num_coord[1]
	for sym_coord in symbol_arr:
		if hit(sym_coord,num_box):
			output = output + num
			break

print(output)