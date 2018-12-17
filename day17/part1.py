import sys
import math
from collections import deque

clay_locs = set()
min_y = math.inf
max_y = -1

# Just for printing help!
min_x, max_x = math.inf, -1

infn = sys.argv[1] if len(sys.argv) > 1 else 'test_input' #'input'
with open(infn) as inf:
    for line in inf:
        parts = line.strip().split()
        part1 = parts[0][:-1]   # part 1 has a comma on it
        part1_val = int(part1[2:])

        part2_rangesplit = parts[1].split('..')
        range_start = int(part2_rangesplit[0][2:])
        range_end = int(part2_rangesplit[1])

        for range_val in range(range_start, range_end+1):
            if part1[0] == 'x':
                min_y = min(min_y, range_val)
                max_y = max(max_y, range_val)
                min_x = min(min_x, part1_val)
                max_x = max(max_x, part1_val)
                clay_locs.add((part1_val, range_val))
            else:
                min_y = min(min_y, part1_val)
                max_y = max(max_y, part1_val)
                min_x = min(min_x, range_val)
                max_x = max(max_x, range_val)
                clay_locs.add((range_val, part1_val))
            # end if
        # end for
    # end for
# end with
water_loc = (500, 0)


def print_map(y_maximum, x_range, _clays, _water, _visited_wet, _outfile=None):
    for y in range(0, y_maximum+1):
        for x in range(x_range[0], x_range[1]+1):
            if (x, y) == water_loc:
                if _outfile is not None:
                    _outfile.write('+')
                else:
                    print('+', end="")
            elif (x, y) in _clays:
                if _outfile is not None:
                    _outfile.write('#')
                else:
                    print('#', end="")
            elif (x, y) in _water:
                if _outfile is not None:
                    _outfile.write('~')
                else:
                    print('~', end="")
            elif (x, y) in _visited_wet:
                if _outfile is not None:
                    _outfile.write('|')
                else:
                    print('|', end="")
            else:
                if _outfile is not None:
                    _outfile.write('.')
                else:
                    print('.', end="")
            # end if
        # end for
        if _outfile is not None:
            _outfile.write('\n')
        else:
            print()
    # end for
# end print_map


print("map runs from {} to {}".format((min_x, min_y), (max_x, max_y)))
print_map(max_y, (min_x, max_x), clay_locs, {}, {})

visited_points = set()
wet_locs = set()
fill_points = deque([water_loc])
its = 0
while len(fill_points) > 0:
    its += 1
    fp = fill_points[-1]

    if fp in clay_locs:
        fill_points.pop()
        continue

    if fp[1] == max_y:
        wet_locs.add(fp)
        fill_points.pop()
        continue

    below_point = (fp[0], fp[1]+1)
    if below_point not in clay_locs and below_point not in wet_locs:
        fill_points.append(below_point)
        continue

    if fp in visited_points:
        fill_points.pop()
        continue
    visited_points.add(fp)

    wet_locs.add(fp)
    fill_points.pop()

    left_point = (fp[0]-1, fp[1])
    below_left = (left_point[0], left_point[1]+1)
    if below_left in clay_locs or below_left in wet_locs:
        fill_points.append(left_point)

    right_point = (fp[0]+1, fp[1])
    below_right = (right_point[0], right_point[1]+1)
    if below_right in clay_locs or below_right in wet_locs:
        fill_points.append(right_point)

    print(fp)
    print()
    if its % 5 == 0:
        print(str(its) + " iterations")
        print(wet_locs)
        print_map(max_y, (min_x, max_x), clay_locs, set(), wet_locs)
        input()
# end for
print("finished")

#with open('output', 'w') as output_file:
print_map(max_y, (min_x, max_x), clay_locs, set(), wet_locs)

# Filter out points outside of our range
wet_locs = set([v for v in wet_locs if v[1] <= max_y and v[1] >= min_y])
print(len(wet_locs))

