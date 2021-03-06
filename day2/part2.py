'''input_lines = []
with open('input', 'r') as input_file:
	for input_line in input_file:
		input_lines.append(input_line)
	#end for
#end with

index_1 = -1
index_2 = -1

# The idea of the loop is to remove characters at given indices one at a time.
# Then, if we sort the list alphabetically (which is python's default string sort),
# the two strings matching our solution, with the right character removed, will be adjacent.
# We can't get a wrong answer, because every other string must fail the equality test
# of the second loop.

# Relies on all strings being the same length. Could probably do better.
for i in range(len(input_lines[0])):
	index_removed_lines = []
	index_in_list = 0
	for inline_index in range(len(input_lines)):
		inline = input_lines[inline_index]
		string_minus_index = inline[:i] + inline[i+1:]
		irl_tuple = (index_in_list, string_minus_index)
		index_removed_lines.append(irl_tuple)
		index_in_list += 1
	#end for
	
	index_removed_lines.sort(key=lambda x: x[1])
	
	# The last string has nothing to compare to
	for j in range(len(index_removed_lines)-1):
		current_line = index_removed_lines[j]
		next_line = index_removed_lines[j+1]
		if current_line[1] == next_line[1]:
			index_1 = current_line[0]
			index_2 = next_line[0]
			break
		#end if
	#end for
	
	if index_1 != -1:
		break
#end for

print(index_1)
print(index_2)
print()
common_characters = []
for one, two in zip(input_lines[index_1], input_lines[index_2]):
	if one == two:
		common_characters.append(one)
	else:
		print("MISMATCHED CHARACTERS:")
		print(one)
		print(two)
		print("END MISMATCHED\n")
#end for
print("".join(common_characters))'''
#^ First solution. Was dumb. Didn't think properly.
# Ended up just making a way worse one! Less code in the below one too!

'''
input_lines = None
with open('input', 'r') as input_file:
	input_lines = input_file.read().splitlines()
#end with

num_lines = len(input_lines)
match_found = False
for line_index1 in range(num_lines):
	line1 = input_lines[line_index1]
	for line_index2 in range(line_index1 + 1, num_lines):
		line2 = input_lines[line_index2]
		
		# Could do the typing manually, but we'll use this to print a nice thing.
		last_diff = -1
		
		num_diffs = 0
		for zip_index, (c1, c2) in enumerate(zip(line1, line2)):
			if c1 != c2:
				last_diff = zip_index
				num_diffs += 1
				if num_diffs > 1: break
			#end if
		#end for
		
		if num_diffs == 1:
			# Match found!
			match_found = True
			print(line1)
			print(line2)
			print("\nMismatched Characters: ({}, {}) - index {}".format(line1[last_diff], line2[last_diff], last_diff))
			print("\nAnswer:", line1[:last_diff] + line1[last_diff+1:])
		#end if
	#end for
	if match_found: break
#end for
'''

# version 3:
input_lines = []
with open('input') as input_file:
	for line in input_file:
		input_lines.append(line)

l_1, l_2 = -1, -1
for i in range(len(input_lines[0])):
	line_map = {}
	
	for j in range(len(input_lines)):
		input_lines_line = input_lines[j]
		string_minus_i = input_lines_line[:i] + input_lines_line[i+1:]
		if string_minus_i in line_map:
			print("{} and {}".format(line_map[string_minus_i], j))
			l_1 = line_map[string_minus_i]
			l_2 = j
			break
		else:
			line_map[string_minus_i] = j
		# end if
	# end for

	if l_1 != -1:
		break
# end for

non_mismatched_chars = [x for x, y in zip(input_lines[l_1], input_lines[l_2]) if x == y]
print("".join(non_mismatched_chars))



