items = {}

with open('input') as input_file:
    for line in input_file:
        line_parts = line.split()
        root = line_parts[1]
        child = line_parts[7]
        if child in items:
            items[child].add(root)
        else:
            items[child] = set(root)

        if root not in items:
            items[root] = set()
    # end for
# end with

num_workers = 5
workers = [(0, '.') for _ in range(num_workers)]
print(workers)


def get_next_item(in_items, visited_items, claimed_items):
    candidates = []
    for iik, iiv in in_items.items():
        if iik in visited_items or iik in claimed_items:
            continue
        if iiv.issubset(visited_items):
            candidates.append(iik)
    # end for
    if len(candidates) == 0:
        return None

    return sorted(candidates)[0]
# end get_next_item


_visited_items = set()
timer = -1
print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format("Second", "Worker1", "Worker2", "Worker3", "Worker4", "Worker5", "Done"))
while len(_visited_items) < len(items):
    timer += 1
    new_visited_items = []
    for worker_i in range(num_workers):
        worker = workers[worker_i]
        if worker[0] <= timer:
            # if we finished an item, add it to our visited list
            if worker[1] != '.':
                new_visited_items.append(worker[1])
    # end for
    for nvi in new_visited_items:
        _visited_items.add(nvi)

    for worker_i in range(num_workers):
        worker = workers[worker_i]
        if worker[0] <= timer:
            next_item = get_next_item(items, _visited_items, [x[1] for x in workers])
            if next_item is not None:
                # 65 is capital A, so ord - 64 is the timer addition
                new_time = timer + 60 + (ord(next_item) - 64)
                workers[worker_i] = (new_time, next_item)
            else:
                workers[worker_i] = (0, '.')

    print("{:04}".format(timer), end="\t\t")
    print("{}({})".format(workers[0][0], workers[0][1]), end="\t\t")
    print("{}({})".format(workers[1][0], workers[1][1]), end="\t\t")
    print("{}({})".format(workers[2][0], workers[2][1]), end="\t\t")
    print("{}({})".format(workers[3][0], workers[3][1]), end="\t\t")
    print("{}({})".format(workers[4][0], workers[4][1]), end="\t\t")
    print("".join(_visited_items))

    print()
# end while

print(_visited_items)
print(timer)


