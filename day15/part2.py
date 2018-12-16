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
        print("{} taking {} damage".format(self, damage))
        self.hp -= damage
        return self.hp > 0
    # end take_damage
# end Unit


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


def get_next_loc(_map, _enemies, _nonenemies, i_loc):
    q = deque([])
    used = {l: False for l in all_locations}
    dist = {l: -1 for l in all_locations}
    parent = {l: None for l in all_locations}

    q.appendleft(i_loc)
    used[i_loc] = True

    while len(q) > 0:
        n_loc = q.popleft()

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


def resolve_battle(resolve_elf_damage):
    opposing_forces_exist = True
    num_rounds = 0
    while opposing_forces_exist:
        for ui, unit in enumerate(unit_it):
            if unit.hp < 1:
                continue

            elves_c = {}
            goblins_c = {}
            for u in unit_it:
                if u.hp < 1:
                    continue
                if u.type == 'E':
                    elves_c[u.x, u.y] = u
                else:
                    goblins_c[u.x, u.y] = u
                # end if
            # end for

            if len(elves_c) < elf_count:
                print("Elf died!")
                pprint_battlefield()
                return -1, -1

            enemy_c = goblins_c if unit.type == 'E' else elves_c
            nonenemy_c = elves_c if unit.type == 'E' else goblins_c

            if len(enemy_c) == 0:
                opposing_forces_exist = False
                break

            current_loc = (unit.x, unit.y)
            c_loc = get_next_loc(battlefield, enemy_c, nonenemy_c, current_loc)
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
                weakest_enemy_l = down
            # end if

            if weakest_enemy_l is not None:
                enemy_c[weakest_enemy_l].take_damage(resolve_elf_damage if unit.type == 'E' else 3)
        # end for

        unit_it.sort(key=lambda u: u.x)
        unit_it.sort(key=lambda u: u.y)
        num_rounds += 1
    # end while

    return num_rounds - 1, sum([u.hp for u in unit_it if u.hp > 0])
# end resolve_battle


num_rounds = -1
remaining_hp = -1
MAX_ITS = 5000
for elf_damage in range(4, MAX_ITS):
    battlefield = []
    unit_it = []
    elf_count = 0
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
                    elf_count += 1
                else:
                    line_list.append(c)
                # end if
            # end for
            battlefield.append(line_list)
            h = y + 1
        # end for
    # end with
    all_locations = list(product(range(w), range(h)))

    print("Resolving elf damage {}".format(elf_damage))
    num_rounds, remaining_hp = resolve_battle(elf_damage)
    if num_rounds > -1:
        break
# end while

print("power {}: {} * {} = {}".format(elf_damage, num_rounds, remaining_hp, num_rounds * remaining_hp))

