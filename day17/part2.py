import sys
import math

clay_locs = set()
min_y, max_y = math.inf, -1

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


def print_map(y_maximum, x_range, _clays, _still_water, _flowing_water, _outfile=None):
    """
    Print the current state of the map, optionally to an output file.
    """
    for y in range(0, y_maximum+1):
        for x in range(x_range[0], x_range[1]+1):
            ch = '.'
            if (x, y) == water_loc:
                ch = '+'
            elif (x, y) in _clays:
                ch = '#'
            elif (x, y) in _still_water:
                ch = '~'
            elif (x, y) in _flowing_water:
                ch = '|'
            # end if

            if _outfile is not None:
                _outfile.write(ch)
            else:
                print(ch, end="")
        # end for
        if _outfile is not None:
            _outfile.write('\n')
        else:
            print()
    # end for
# end print_map


def find_fall(fall_p, _max_y, _clays, _flowing):
    """
    Find the last point in the fall from given position, fall_p, with a max depth of _max_y.
    Return that point, or None if it does not exist (a.k.a. we pass _max_y).
    Also, keep an updated output list of flowing water squares, in _flowing.
    :param fall_p:      the initial position to fall from. Form of (x, y)
    :param _max_y:      the deepest distance we'll iterate to
    :param _clays:      the set of all known clay locations
    :param _flowing:    the set of all known flowing water locations, updated for output
    :return:            the last point found in this fall. Above either clay or the max depth.
    """
    while fall_p[1] < _max_y:
        fall_p_d = (fall_p[0], fall_p[1]+1)
        if fall_p_d in _clays:
            return fall_p

        _flowing.add(fall_p_d)
        fall_p = fall_p_d
    # end while

    return None
# end find_fall


def spread_horizontal(p, direction, _clays, _still_water, discovered_water):
    """
    The horizontal portion of our spread. Starting at the given p,
    iterate in the given direction until a wall is found, or a square
    with a missing bottom is found.
    :param p:                   the initial position. An (x, y) tuple
    :param direction:           the direction to iterate in. An (x, y) tuple
    :param _clays:              the set of all clay blocks
    :param _still_water:        the set of all known 'still water' blocks
    :param discovered_water:    an output set of all water found by this spread
    :return:                    the point at the end of the spread, IFF it's a fall point. Otherwise None
    """
    it_p = p
    while it_p not in _clays:
        discovered_water.add(it_p)
        below_p = (it_p[0], it_p[1]+1)
        if below_p not in _clays and below_p not in _still_water:
            return it_p
        it_p = (it_p[0] + direction[0], it_p[1] + direction[1])
    # end while
    return None
# end spread_recurse


def spread(p, _clays, _flowing, _still_water):
    """
    Do a spread from given point p. This encapsulates both horizontal directions.
    :param p:               the position to spread from
    :param _clays:          the set of known clay locations
    :param _flowing:        output set to add newly discovered flowing water squares
    :param _still_water:    used to detect fall locations, and updated with newly discovered still water squares
    :return:
    """
    horizontal_spread_squares = set()

    # do the two horizontal spreads.
    p_left = spread_horizontal(p, (-1, 0), _clays, _still_water, horizontal_spread_squares)
    p_right = spread_horizontal(p, (1, 0), _clays, _still_water, horizontal_spread_squares)

    # If no fall point was found on either side, this is standing water, so add it to the still water list.
    if p_left is None and p_right is None:
        _still_water.update(horizontal_spread_squares)
    else:
        # Else this water won't stay still, so update the flowing list instead
        _flowing.update(horizontal_spread_squares)

    # Return our points no matter their values. Our parent can also use Nones for useful info.
    return p_left, p_right
# end spread


print("map runs from {} to {}".format((min_x, min_y), (max_x, max_y)))
print_map(max_y, (min_x, max_x), clay_locs, {}, {})

# Actual output sets.
flowing_locs, still_locs = set(), set()

# Sets just for iteration help.
to_fall = {water_loc}
to_spread = set()

while to_fall or to_spread:
    # First do all of the falling that we know about
    while to_fall:
        tfp = to_fall.pop()
        fall_result = find_fall(tfp, max_y, clay_locs, flowing_locs)
        if fall_result is not None:
            to_spread.add(fall_result)
    # end while

    # Now that falling is done, do spreading. We may find new fall points for our next loop.
    while to_spread:
        tsp = to_spread.pop()
        r_left, r_right = spread(tsp, clay_locs, flowing_locs, still_locs)

        if r_left is not None:
            to_fall.add(r_left)

        if r_right is not None:
            to_fall.add(r_right)

        if r_left is None and r_right is None:
            tsp_above = (tsp[0], tsp[1]-1)
            to_spread.add(tsp_above)
        # end if
    # end while
# end while

print_map(max_y, (min_x, max_x), clay_locs, still_locs, flowing_locs)

# Filter out points outside of our range
wet_locs = set([v for v in still_locs if v[1] <= max_y and v[1] >= min_y])
print(len(wet_locs))

