
num_twos = 0
num_threes = 0

with open('input', 'r') as input_file:
	for input_line in input_file:
		input_histogram = {}
		for input_character in input_line:
			if input_character in input_histogram:
				input_histogram[input_character] += 1
			else:
				input_histogram[input_character] = 1
			#end if
		#end for
		two_found = False
		three_found = False
		for k, v in input_histogram.items():
			if v == 2:
				two_found = True
			elif v == 3:
				three_found = True
			#endif
		#end for
		if two_found:
			num_twos += 1
		if three_found:
			num_threes += 1
	#end for
#end with

checksum = num_twos * num_threes
print(checksum)
