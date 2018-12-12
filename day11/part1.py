serial = 4455
#serial = 18


def calculate_power(x, y):
    rack_id = x + 10

    power = y * rack_id
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    power -= 5

    return power
# end calculate_power


powers = []
for x in range(1, 301):
    for y in range(1, 301):
        cp = calculate_power(x, y)
        powers.append(cp)
        if x == 1 and y == 1: print(cp)
    # end for
    #print()
# end for
print()
cube_powers = {}
for x in range(0, 298):
    for y in range(0, 298):
        pi = x + (y * 300)
        #print(pi)
        cube_power = powers[pi]
        cube_power += powers[pi + 1]
        cube_power += powers[pi + 2]
        cube_power += powers[pi + 300]
        cube_power += powers[pi + 301]
        cube_power += powers[pi + 302]
        cube_power += powers[pi + 600]
        cube_power += powers[pi + 601]
        cube_power += powers[pi + 602]
        cube_powers[cube_power] = (x+1, y+1)
        #print(x, y, cube_power)
    # end for
# end for
print()
max_power = max(cube_powers.keys())
coords = cube_powers[max_power]
print(max_power, coords)


