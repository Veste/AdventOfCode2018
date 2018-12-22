TEST_OFFSETS = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
]
OPEN = '.'
TREE = '|'
LUMBERYARD = '#'


def convert_open(location, _current_map):
    num_trees = 0
    for offset in TEST_OFFSETS:
        offset_location = (location[0] + offset[0], location[1] + offset[1])
        if offset_location[0] < 0 or offset_location[0] >= len(_current_map[0])\
            or offset_location[1] < 0 or offset_location[1] >= len(_current_map):
            continue
        # end if

        if _current_map[offset_location[1]][offset_location[0]] == TREE:
            num_trees += 1
        # end if

        # could early out but, eh.
    # end for

    return TREE if num_trees > 2 else OPEN
# end convert_open


def convert_tree(location, _current_map):
    num_lumberyards = 0
    for offset in TEST_OFFSETS:
        offset_location = (location[0] + offset[0], location[1] + offset[1])
        if offset_location[0] < 0 or offset_location[0] >= len(_current_map[0])\
            or offset_location[1] < 0 or offset_location[1] >= len(_current_map):
            continue
        # end if

        if _current_map[offset_location[1]][offset_location[0]] == LUMBERYARD:
            num_lumberyards += 1
        # end if

        # could early out but, eh.
    # end for

    return LUMBERYARD if num_lumberyards > 2 else TREE
# end convert_tree


def convert_lumberyard(location, _current_map):
    num_lumberyards = 0
    num_trees = 0
    for offset in TEST_OFFSETS:
        offset_location = (location[0] + offset[0], location[1] + offset[1])
        if offset_location[0] < 0 or offset_location[0] >= len(_current_map[0])\
            or offset_location[1] < 0 or offset_location[1] >= len(_current_map):
            continue
        # end if

        if _current_map[offset_location[1]][offset_location[0]] == LUMBERYARD:
            num_lumberyards += 1
        # end if

        if _current_map[offset_location[1]][offset_location[0]] == TREE:
            num_trees += 1
        # end if

        # could early out but, eh.
    # end for

    return OPEN if (num_lumberyards == 0 or num_trees == 0) else LUMBERYARD
# end convert_lumberyard


tree_map = []
infn = 'input'
with open(infn) as inf:
    for line in inf:
        row_vals = []
        for c in line.strip():
            row_vals.append(c)
        # end for
        tree_map.append(row_vals)
    # end for
# end with

with open('outfile', 'w') as out_file:
    out_file.write("\n")
# end with

product_at_500 = -1
period = -1
products = []
SPACE_OPERATION_MAP = {OPEN: convert_open, TREE: convert_tree, LUMBERYARD: convert_lumberyard}

# Make sure we sample enough data to guarantee a period.
for minute in range(1, 10000):

    next_minute_map = []
    for y in range(len(tree_map)):
        nm_row = []
        for x in range(len(tree_map[0])):
            type_in_map = tree_map[y][x]
            nm_row.append(SPACE_OPERATION_MAP[type_in_map]((x, y), tree_map))
        # end for
        next_minute_map.append(nm_row)
    # end for
    tree_map = next_minute_map

    if minute >= 500:
        num_trees = 0
        num_lumberyards = 0
        for r in tree_map:
            for p in r:
                if p == TREE:
                    num_trees += 1
                elif p == LUMBERYARD:
                    num_lumberyards += 1
        # end for
        product = num_trees * num_lumberyards
        if minute == 500:
            product_at_500 = product
        elif product - product_at_500 == 0:
            print(minute)
            period = minute - 500
            break

        products.append(product)
# end for

print(products)

# Have to subtract the minute where we started tracking our period, because that's when the period we listed repeats!
# Basically, from minute 500, there's a period, which we explicitly defined to start at 500 (detected via manual data
# visualization). So if we figure out which modulus of the length the 1000000000th minute is RELATIVE to 500, we'll
# have our answer.
print(products[(1000000000 - 500) % len(products)])

