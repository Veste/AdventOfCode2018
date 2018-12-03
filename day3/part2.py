# problem says fabric is a 1000x1000 square
fabric = [[[] for x in range(1000)] for y in range(1000)]


def update_fabric(x, y, w, h, claim_num):
    for x_val in range(x, x + w):
        for y_val in range(y, y + h):
            fabric[y_val][x_val].append(claim_num)
# end update_fabric


# Python lists start at 0, but the claim numbers start at 1.
# So here's a dummy True value to make the indexes line up without +/-1s.
claim_seen_overlapped = [True]


with open('input', 'r') as input_file:
    for line in input_file:
        claim_seen_overlapped.append(False)

        split_line = line.split()

        claim_num_ = int(split_line[0][1:])

        xy_part = split_line[2].split(',')
        x_, y_ = int(xy_part[0]), int(xy_part[1][:-1])

        wh_part = split_line[3].split('x')
        w_, h_ = int(wh_part[0]), int(wh_part[1])

        update_fabric(x_, y_, w_, h_, claim_num_)
    # end for
# end with


for row in fabric:
    for claims in row:
        if len(claims) < 2:
            continue

        for claim in claims:
            claim_seen_overlapped[claim] = True
    # end for
# end for


good_claim_index = claim_seen_overlapped.index(False)
print(good_claim_index)
