serial = 4455
#serial = 18
#serial = 42


def calculate_power(x, y):
    rack_id = x + 10

    power = y * rack_id
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    power -= 5

    return power
# end calculate_power


powers = {}
for x in range(1, 301):
    for y in range(1, 301):
        cp = calculate_power(x, y)
        powers[x - 1, y - 1] = cp
    # end for
# end for

max_power = 0
max_power_coords = None
max_power_size = None
ps_powers = None
next_powers = powers

for size in range(2, 301):
    print(size)
    ps_powers = next_powers
    next_powers = {}
    for x in range(0, 301-size):
        for y in range(0, 301-size):
            new_power = ps_powers[x, y]
            for rci in range(0, size - 1): # row/column index
                new_power += powers[x + rci, y + size - 1]
                new_power += powers[x + size - 1, y + rci]
            # end for
            # For loop leaves off the bottom right corner, so add that too
            new_power += powers[x + size - 1, y + size - 1]
            next_powers[x, y] = new_power
            if new_power > max_power:
                max_power = new_power
                max_power_coords = x + 1, y + 1
                max_power_size = size
            # end if
        # end for
    # end for
# end for


print(max_power, max_power_coords, max_power_size)


