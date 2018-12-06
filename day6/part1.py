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

print(leftmost, rightmost, topmost, bottommost)

bad_list = [leftmost, rightmost, topmost, bottommost]

def man_dist(p, x, y):
    return abs(p[0] - x) + abs(p[1] - y)
# end man_dist


count_map = {k: 0 for k in coordinate_list}

with open('output', 'w') as out_file:
    for x_val in range(leftmost[0], rightmost[0] + 1):
        for y_val in range(topmost[1], bottommost[1] + 1):
            points_in_closest_order = sorted(coordinate_list, key=lambda p: man_dist(p, x_val, y_val))
            closest_point = points_in_closest_order[0]

            first_closest_distance = man_dist(points_in_closest_order[0], x_val, y_val)

            # print("{}".format(coordinate_list.index(closest_point)), end=" ")
            format_string = "{:4} "
            if first_closest_distance == 0:
                format_string = "[{:2}] "
            # out_file.write(format_string.format(coordinate_list.index(closest_point)))

            second_closest_distance = man_dist(points_in_closest_order[1], x_val, y_val)
            if first_closest_distance == second_closest_distance:
                out_file.write("   . ")
                continue
            else:
                out_file.write(format_string.format(coordinate_list.index(closest_point)))

            if closest_point not in bad_list:
                if x_val == leftmost[0] or x_val == rightmost[0] or y_val == topmost[1] or y_val == bottommost[1]:
                    bad_list.append(closest_point)
                else:
                    count_map[closest_point] += 1
        out_file.write('\n')
    # end for

print(count_map)

highest_count = 0
for k,v in count_map.items():
    if k in bad_list:
        continue

    if v > highest_count:
        print(k)
        highest_count = v

print(highest_count)

