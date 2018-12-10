input_elements_str = None
with open('input') as input_file:
    input_elements_str = input_file.readline().split()
# end with
input_elements = [int(e) for e in input_elements_str]


def process_node(e, num_nodes):
    if num_nodes == 0:
        return 0

    i = 0
    running_sum = 0
    processed = 0
    while processed < num_nodes:
        n_c, n_m = e[i], e[i+1]
        processed += 1
        if n_c == 0:
            running_sum += sum(e[i+2:i+2+n_m])
            i += 2 + n_m
        else:
            subnode_final_index, subnode_sum = process_node(e[i+2:], n_c)
            running_sum += subnode_sum
            running_sum += sum(e[subnode_final_index:subnode_final_index+n_m])
            i = subnode_final_index + n_m
        # end if
    # end while

    return i, running_sum
# end process_node


running_sum = 0
ni = 0
node_stack = []
while ni < len(input_elements):
    if len(node_stack) > 0 and node_stack[-1][0] == 0:
        stack_top = node_stack.pop()
        running_sum += sum(input_elements[ni:ni + stack_top[1]])
        ni += stack_top[1]
        if len(node_stack) == 0: break
        node_stack[-1][0] -= 1
    else:
        node_stack.append([input_elements[ni], input_elements[ni+1]])
        ni += 2
    # end if
# end while

print(running_sum)


