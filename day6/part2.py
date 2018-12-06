coordinate_list = []

with open('input') as input_file:
    for line in input_file:
        coords = line.split()
        coordinate_list.append((int(coords[0][:-1]), int(coords[1])))
    # end for
# end with

print(coordinate_list)

leftmost = min(coordinate_list, key=lambda x: x[0])
rightmost = max(coordinate_list, key=lambda x: x[0])
topmost = min(coordinate_list, key=lambda y: y[1])
bottommost = max(coordinate_list, key=lambda y: y[1])

max_region_dist = 10000
left_edge = leftmost[0] - 500
right_edge = rightmost[0] + 500
top_edge = topmost[1] - 500
bottom_edge = bottommost[1] + 500


def man_dist(p, x, y):
    return abs(p[0] - x) + abs(p[1] - y)
# end man_dist


count_map = {k: 0 for k in coordinate_list}
region_size = 0
with open('output_2', 'w') as out_file:
    for x_val in range(left_edge, right_edge + 1):
        for y_val in range(top_edge, bottom_edge + 1):
            # total_distance = sum([man_dist(p, x_val, y_val) for p in coordinate_list])
            total_distance = 0
            for coord in coordinate_list:
                total_distance += man_dist(coord, x_val, y_val)
                if total_distance > max_region_dist:
                    break

            if total_distance < max_region_dist:
                out_file.write("# ")
                region_size += 1
            else:
                out_file.write(". ")
        # end for
        out_file.write('\n')
    # end for
# end with

print("finished", region_size)


