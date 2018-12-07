items = {}

with open('input') as input_file:
    for line in input_file:
        line_parts = line.split()
        root = line_parts[1]
        child = line_parts[7]
        if child in items:
            items[child].append(root)
        else:
            items[child] = [root]

        if root not in items:
            items[root] = []
    # end for
# end with

for kk, vv in items.items():
    print(kk, vv)

visited_items = []

while len(visited_items) < len(items):
    found_items_for_iteration = []

    for key, value in items.items():
        if key in visited_items:
            continue

        for visited_item in visited_items:
            if visited_item in value:
                value.remove(visited_item)
        # end for

        if len(value) == 0:
            found_items_for_iteration.append(key)
        # end if
    # end for

    visited_items.append(sorted(found_items_for_iteration)[0])
    print("{} : {}".format("".join(found_items_for_iteration), "".join(visited_items)))
# end while

print("".join(visited_items))

