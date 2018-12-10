pandvs = []
max_x, min_x = 0, 0
max_y, min_y = 0, 0
with open('input') as in_f:
    for in_l in in_f:
        l_split = in_l.split(',')
        pos_x = int(l_split[0][10:].strip())
        max_x = max(max_x, pos_x)
        min_x = min(min_x, pos_x)

        pos_y = int(l_split[1][:7].strip())
        max_y = max(max_y, pos_y)
        min_y = min(min_y, pos_y)

        vel_x = int(l_split[1][-2:].strip())
        vel_y = int(l_split[2][:3].strip())
        pandvs.append([ [pos_x, pos_y], [vel_x, vel_y] ])
    # end for
# end with


def print_visualization(vis):
    for row in vis:
        for p in row:
            print(p, end="")
        # end for
        print()
    # end for
    print()
# end add_to_visualizations


x_distance = max_x - min_x
y_distance = max_y - min_y
s = 'b'
XLIMIT = 100
YLIMIT = 100
num_its = 0
while s != 'a':
    num_its += 1
    print(x_distance, y_distance)
    for pv in pandvs:
        pv[0][0] += pv[1][0]
        pv[0][1] += pv[1][1]
    # end for
    max_x = max(pandvs, key=lambda p: p[0][0])[0][0]
    min_x = min(pandvs, key=lambda p: p[0][0])[0][0]
    max_y = max(pandvs, key=lambda p: p[0][1])[0][1]
    min_y = min(pandvs, key=lambda p: p[0][1])[0][1]
    if x_distance < XLIMIT and y_distance < YLIMIT:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                point = [p for p in pandvs if p[0] == [x, y]]
                if len(point) > 0:
                    print('#', end='')
                else:
                    print('.', end='')
                # end if
            # end for y
            print()
        # end for x
        print(num_its)
        s = input('it second; "a" stop')
    # end if
    x_distance = max_x - min_x
    y_distance = max_y - min_y
# end while

print("ended:", x_distance, y_distance, s, num_its)


