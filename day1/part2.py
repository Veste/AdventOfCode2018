total_frequency = 0
frequency_set = set()

with open("input_1", 'r') as input_file:
	duplicate_found = False
	while not duplicate_found:
		for line in input_file:
			
			frequency_number = int(line[1:])
			if line[0] == '+':
				total_frequency += frequency_number
			elif line[0] == '-':
				total_frequency -= frequency_number
			#end if
			
			if total_frequency in frequency_set:
				print("First twice-seen frequency is:", total_frequency)
				duplicate_found = True
				break
			else:
				#print("Not seen:", total_frequency)
				frequency_set.add(total_frequency)
			#end if
		#end for
		
		input_file.seek(0)
	#end while
#end with
