def reduce_line(input_line):
    workspace_line = input_line
    i = 0
    while i != len(workspace_line) - 1:
        c = workspace_line[i]
        n_c = workspace_line[i + 1]

        if ord(n_c) == ord(c) - 32 or ord(n_c) == ord(c) + 32:
            workspace_line = workspace_line[:i] + workspace_line[i + 2:]
            if i > 0:
                # If we're not the first, we need to step back to check again
                i -= 2

        i += 1
    # end while

    return workspace_line
# end reduce_line


def remove_char_from_line(lowercase_char, input_line):
    return input_line.replace(lowercase_char, "").replace(lowercase_char.upper(), "")
# end remove_char_from_line


input_file_line = None
with open('input') as input_file:
    input_file_line = input_file.readline()
# end with

all_lowercase_chars = list(map(chr, range(97, 123)))
shortest_result = len(input_file_line)
for character in all_lowercase_chars:
    new_string = reduce_line(remove_char_from_line(character, input_file_line))
    new_string_len = len(new_string)
    if new_string_len < shortest_result:
        print("{}\n".format(new_string))
        shortest_result = new_string_len
    # end if
# end for

print(shortest_result)

