input_line = ""
with open('input') as input_file:
    for line in input_file:
        input_line = line
# end with
workspace_line = input_line
i = 0
while i != len(workspace_line) - 1:
    c = workspace_line[i]
    n_c = workspace_line[i+1]

    if ord(n_c) == ord(c) - 32 or ord(n_c) == ord(c) + 32:
        workspace_line = workspace_line[:i] + workspace_line[i+2:]
        if i > 0:
            # If we're not the first, we need to step back to check again
            i -= 2
    # end if

    i += 1
# end while

print(workspace_line)
print(len(workspace_line))

