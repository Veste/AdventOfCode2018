
# problem says fabric is a 1000x1000 square
fabric = [[0 for x in range(1000)] for y in range(1000)]


def update_fabric(x, y, w, h):
    for x_val in range(x, x + w):
        for y_val in range(y, y + h):
            fabric[y_val][x_val] += 1
# end update_fabric


with open('input', 'r') as input_file:
    for line in input_file:
        split_line = line.split()

        xy_part = split_line[2].split(',')
        x_, y_ = int(xy_part[0]), int(xy_part[1][:-1])

        wh_part = split_line[3].split('x')
        w_, h_ = int(wh_part[0]), int(wh_part[1])

        update_fabric(x_, y_, w_, h_)
    # end for
# end with

total_shared = 0
for inch_row in fabric:
    for inch in inch_row:
        if inch > 1:
            total_shared += 1
# end for

print(total_shared)

