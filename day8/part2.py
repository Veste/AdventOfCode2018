input_elements_str = None
with open('input') as input_file:
    input_elements_str = input_file.readline().split()
# end with
input_elements = [int(e) for e in input_elements_str]

#input_elements = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

running_sum = 0
ni = 0
node_stack = []


while ni < len(input_elements):
    if len(node_stack) > 0 and node_stack[-1][0] == 0:
        stack_top = node_stack.pop()

        this_node_sum = 0
        meta_list = input_elements[ni:ni + stack_top[1]]
        if len(stack_top[2]) == 0:
            this_node_sum = sum(meta_list)
            print("regular sum:", this_node_sum)
        else:
            print(meta_list)
            for child_ref in meta_list:
                if child_ref > 0 and child_ref <= len(stack_top[2]):
                    print(stack_top[2][child_ref - 1])
                    this_node_sum += stack_top[2][child_ref - 1]
        # end if
        running_sum += this_node_sum

        ni += stack_top[1]
        if len(node_stack) == 0:
            print("answer:", this_node_sum)
            break
        node_stack[-1][0] -= 1
        node_stack[-1][2].append(this_node_sum)
    else:
        node_stack.append([input_elements[ni], input_elements[ni+1], []])
        ni += 2
    # end if
# end while

# NOT 27235
print(running_sum)


