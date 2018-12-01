total_frequency = 0

with open("input_1", 'r') as input_file:
	for line in input_file:
		frequency_number = int(line[1:])
		if line[0] == '+':
			total_frequency += frequency_number
		elif line[0] == '-':
			total_frequency -= frequency_number
		#end if
	#end for
#end with

print("Total frequency is:", total_frequency)