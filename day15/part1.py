from collections import deque
from itertools import product

infn = 'input'
#infn = 'input_t6'
#infn = 'input_t5'
#infn = 'input_t4'
#infn = 'input_t3'
#infn = 'input_t2'
#infn = 'input_t1'


class Unit:
    def __init__(self, location, in_type):
        self.x = location[0]
        self.y = location[1]
        self.type = in_type
        self.hp = 200
        self.attack = 3
    # end __init

    def __repr__(self):
        return "Unit({}: [{},{}]; {}hp)".format(self.type, self.x, self.y, self.hp)
    # end __repr__

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.type == other.type)
    # end __eq__

    def __hash__(self):
        return hash((self.x, self.y, self.type))
    # end __hash__

    def take_damage(self, damage):
        self.hp -= damage
        return self.hp > 0
    # end take_damage
# end Unit


battlefield = []
unit_it = []
h, w = -1, -1
with open(infn) as inf:
    for y, line in enumerate(inf):
        line_list = []
        for x, c in enumerate(line.strip()):
            w = x + 1
            new_unit = Unit((x, y), c)
            if c == 'G':
                unit_it.append(new_unit)
                line_list.append('.')
            elif c == 'E':
                unit_it.append(new_unit)
                line_list.append('.')
            else:
                line_list.append(c)
            # end if
        # end for
        battlefield.append(line_list)
        h = y + 1
    # end for
# end with


def pprint_battlefield():
    for y in range(h):
        for x in range(w):
            units_at_loc = [u for u in unit_it if u.x == x and u.y == y and u.hp > 0]
            if len(units_at_loc) > 0:
                print(units_at_loc[0].type, end="")
            else:
                print(battlefield[y][x], end="")
            # end if
        # end for
        print("\t\t", end="")
        for u in sorted([u for u in unit_it if u.y == y], key=lambda u: u.x):
            print(u, end=", ")

        print()
    # end for

    print(unit_it)
# end pprint


print(h, w)
all_locations = list(product(range(w), range(h)))

print(unit_it)
for r in battlefield:
    print(r)
# end for

pprint_battlefield()
#wait = input('wait')


def get_next_loc(_map, _enemies, _nonenemies, i_loc):
    q = deque([])
    used = {l: False for l in all_locations}
    dist = {l: -1 for l in all_locations}
    parent = {l: None for l in all_locations}

    q.appendleft(i_loc)
    used[i_loc] = True

    while len(q) > 0:
        #print(q)
        n_loc = q.popleft()
        #print("{}; used {}".format(n_loc, {k: v for (k, v) in used.items() if v}))

        if n_loc in _enemies:
            # First one we find should be the closest.
            loc = n_loc
            if loc == i_loc or parent[loc] == i_loc:
                return i_loc
            else:
                while parent[loc] != i_loc:
                    loc = parent[loc]
                return loc
        # end if

        if n_loc[1] > 0:
            up = (n_loc[0], n_loc[1]-1)
            if not used[up] and _map[up[1]][up[0]] != '#' and up not in _nonenemies:
                q.append(up)
                dist[up] = dist[n_loc] + 1
                parent[up] = n_loc
                used[up] = True
            # end if
        # end if
        if n_loc[0] > 0:
            left = (n_loc[0]-1, n_loc[1])
            if not used[left] and _map[left[1]][left[0]] != '#' and left not in _nonenemies:
                q.append(left)
                dist[left] = dist[n_loc] + 1
                parent[left] = n_loc
                used[left] = True
            # end if
        # end if
        if n_loc[0]+1 < w:
            right = (n_loc[0]+1, n_loc[1])
            if not used[right] and _map[right[1]][right[0]] != '#' and right not in _nonenemies:
                q.append(right)
                dist[right] = dist[n_loc] + 1
                parent[right] = n_loc
                used[right] = True
            # end if
        # end if
        if n_loc[1]+1 < h:
            down = (n_loc[0], n_loc[1]+1)
            if not used[down] and _map[down[1]][down[0]] != '#' and down not in _nonenemies:
                q.append(down)
                dist[down] = dist[n_loc] + 1
                parent[down] = n_loc
                used[down] = True
            # end if
        # end if
    # end while

    return i_loc
# end find_closest_enemy


opposing_forces_exist = True
num_rounds = 0
while opposing_forces_exist:
    print("Round {}".format(num_rounds))
    for ui, unit in enumerate(unit_it):
        if unit.hp < 1:
            continue
        #print(unit)

        enemy_c = {}
        nonenemy_c = {}
        for u in unit_it:
            if u.hp < 1:
                continue
            if u.type == unit.type:
                nonenemy_c[u.x, u.y] = u
            else:
                enemy_c[u.x, u.y] = u
            # end if
        # end for

        if len(enemy_c) == 0:
            opposing_forces_exist = False
            break

        current_loc = (unit.x, unit.y)
        c_loc = get_next_loc(battlefield, enemy_c, nonenemy_c, current_loc)
        #print("Moving {} to {}".format(current_loc, c_loc))
        unit_it[ui].x = c_loc[0]
        unit_it[ui].y = c_loc[1]

        weakest_enemy_hp = 300
        weakest_enemy_l = None

        up = (unit_it[ui].x, unit_it[ui].y-1)
        if up in enemy_c:
            weakest_enemy_hp = enemy_c[up].hp
            weakest_enemy_l = up

        left = (unit_it[ui].x-1, unit_it[ui].y)
        if left in enemy_c and enemy_c[left].hp < weakest_enemy_hp:
            weakest_enemy_hp = enemy_c[left].hp
            weakest_enemy_l = left

        right = (unit_it[ui].x+1, unit_it[ui].y)
        if right in enemy_c and enemy_c[right].hp < weakest_enemy_hp:
            weakest_enemy_hp = enemy_c[right].hp
            weakest_enemy_l = right

        down = (unit_it[ui].x, unit_it[ui].y+1)
        if down in enemy_c and enemy_c[down].hp < weakest_enemy_hp:
            weakest_enemy_hp = enemy_c[down].hp
            weakest_enemy_l = down
        # end if

        if weakest_enemy_l is not None:
            enemy_c[weakest_enemy_l].take_damage(unit_it[ui].attack)
    # end for
    pprint_battlefield()
    #input()
    print()
    unit_it.sort(key=lambda u: u.x)
    unit_it.sort(key=lambda u: u.y)
    num_rounds += 1
# end while

pprint_battlefield()
print(unit_it)
remaining_hp = sum([u.hp for u in unit_it if u.hp > 0])
print("{} * {} = {}".format(num_rounds-1, remaining_hp, (num_rounds-1) * remaining_hp))


