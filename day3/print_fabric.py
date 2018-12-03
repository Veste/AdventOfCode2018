fabric = [[[] for x in range(1000)] for y in range(1000)]


def update_fabric(x, y, w, h, claim_num):
    for x_val in range(x, x + w):
        for y_val in range(y, y + h):
            fabric[y_val][x_val].append(claim_num)
# end update_fabric


with open('input', 'r') as input_file:
    for line in input_file:
        split_line = line.split()

        claim_num_ = int(split_line[0][1:])

        xy_part = split_line[2].split(',')
        x_, y_ = int(xy_part[0]), int(xy_part[1][:-1])

        wh_part = split_line[3].split('x')
        w_, h_ = int(wh_part[0]), int(wh_part[1])

        update_fabric(x_, y_, w_, h_, claim_num_)
    # end for
# end with


with open('print_fabric_output', 'w') as output_file:
    for row in fabric:
        for item in row:
            if len(item) == 0:
                print('-', end='', file=output_file)
            elif len(item) == 1:
                print('O', end='', file=output_file)
            else:
                print('X', end='', file=output_file)
            # end if
        # end for
        print(file=output_file)
    # end for
# end with


