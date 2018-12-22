import sys
import math

clay_locs = set()
min_y = math.inf
max_y = -1

# Just for printing help!
min_x, max_x = math.inf, -1

infn = sys.argv[1] if len(sys.argv) > 1 else 'input'
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


def find_fall(fall_p, _max_y, _clays, _flowing):
    while fall_p[1] < _max_y:
        fall_p_d = (fall_p[0], fall_p[1]+1)
        if fall_p_d in _clays:
            return fall_p
        _flowing.add(fall_p_d)
        fall_p = fall_p_d
    # end while
    return None
# end find_fall


def spread_recurse(p, offset, _clays, _still_water, r_return):
    it_p = p
    while it_p not in _clays:
        r_return.add(it_p)
        below_p = (it_p[0], it_p[1]+1)
        if below_p not in _clays and below_p not in _still_water:
            return it_p
        it_p = (it_p[0] + offset[0], it_p[1] + offset[1])
    # end while
    return None
# end spread_recurse


def spread(p, _clays, _flowing, _still_water):
    r_results = set()
    p_left = spread_recurse(p, (-1, 0), _clays, _still_water, r_results)
    p_right = spread_recurse(p, (1, 0), _clays, _still_water, r_results)
    if p_left is None and p_right is None:
        _still_water.update(r_results)
    else:
        _flowing.update(r_results)
    return p_left, p_right
# end spread


print("map runs from {} to {}".format((min_x, min_y), (max_x, max_y)))
print_map(max_y, (min_x, max_x), clay_locs, {}, {})

flowing_locs, still_locs, to_fall, to_spread = set(), set(), set(), set()
# Because python sucks at recursion - need to do it manually
to_fall.add(water_loc)
while to_fall or to_spread:
    while to_fall:
        tfp = to_fall.pop()
        fall_result = find_fall(tfp, max_y, clay_locs, flowing_locs)
        if fall_result:
            to_spread.add(fall_result)
    while to_spread:
        tsp = to_spread.pop()
        r_left, r_right = spread(tsp, clay_locs, flowing_locs, still_locs)
        if r_left is None and r_right is None:
            to_spread.add((tsp[0], tsp[1]-1))
        else:
            if r_left is not None:
                to_fall.add(r_left)
            if r_right is not None:
                to_fall.add(r_right)

print_map(max_y, (min_x, max_x), clay_locs, still_locs, flowing_locs)

# Filter out points outside of our range
wet_locs = set([v for v in (flowing_locs | still_locs) if v[1] <= max_y and v[1] >= min_y])
print(len(wet_locs))

