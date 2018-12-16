from collections import deque

state = None
rules = {}

with open('input') as inf:
#with open('test_input') as inf:
    inf_lines = [l.strip() for l in inf.readlines()]

    init_state_str = inf_lines[0][15:]

    state = deque([])
    for i, c in enumerate(init_state_str):
        state.append([c, i])
    # end for
    state.appendleft(['.', state[0][1] - 1])
    state.appendleft(['.', state[0][1] - 1])
    state.append(['.', state[-1][1] + 1])
    state.append(['.', state[-1][1] + 1])

    for rulestr in inf_lines[2:]:
        rssp = rulestr.split(" => ")
        rules[rssp[0]] = rssp[1]
    # end for
# end with
print(state)
for s in state:
    print(s[0], end="")
print()

'''
print(inf_lines)
print(state)
for rule,res in rules.items():
    print(rule, res)
# end for
print()
'''
last_10_states = [state]


plant_total = 0
for v in [-40, -39, -38, -28, -27, -26, -15, -14, -13, 38, 39, 40, 50, 51, 52, 60, 61, 62, 95, 96, 97]:
    plant_total += (49999999999 + v)
# end for
print(plant_total)
exit()


for b in range(50000000000):
    '''
    while state[0][0] == '.':
        state.popleft()
    state.appendleft(['.', state[0][1] - 1])
    state.appendleft(['.', state[0][1] - 1])
    '''

    if b % 100 == 0:
        print(b, end=", ")
        print("".join([s[0] for s in state]))

    prev_state = state
    state = deque([])
    for i in range(len(prev_state)):
        ppc = '.' if i - 2 < 0 else prev_state[i-2][0]
        pc = '.' if i - 1 < 0 else prev_state[i-1][0]
        nc = '.' if i + 1 >= len(prev_state) else prev_state[i+1][0]
        nnc = '.' if i + 2 >= len(prev_state) else prev_state[i+2][0]
        current_string = "".join([
            ppc,
            pc,
            prev_state[i][0],
            nc,
            nnc
        ])
        if current_string in rules:
            state.append([rules[current_string], prev_state[i][1]])
        else:
            state.append(['.', prev_state[i][1]])
        # end if
    # end for

    if state[0][0] == '#' or state[1][0] == '#':
        state.appendleft(['.', state[0][1] - 1])
        state.appendleft(['.', state[0][1] - 1])

    if state[-1][0] == '#' or state[-2][0] == '#':
        state.append(['.', state[-1][1] + 1])
        state.append(['.', state[-1][1] + 1])

    '''
    for s in state:
        print(s[0], end="")
    print()

    ddd = input("wait")
    '''

    plant_total = 0
    if b % 1000 == 0 or b == 20:
        for s in state:
            if s[0] == '#':
                print(s[1] - b, end=", ")
                plant_total += s[1]
        print()
        print(plant_total)
        plant_total = 0
        for v in [-40, -39, -38, -28, -27, -26, -15, -14, -13, 38, 39, 40, 50, 51, 52, 60, 61, 62, 95, 96, 97]:
            plant_total += (b + v)
        # end for
        print("or, ", plant_total)
# end for

plant_total = 0
for s in state:
    print(s[1])
    if s[0] == '#':
        plant_total += s[1]
print(plant_total)


