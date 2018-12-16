in_num = [5,1,5,8,9] # 9
in_num = [0,1,2,4,5] # 5
in_num = [9,2,5,1,0] # 18
in_num = [5,9,4,1,4] # 2018
in_num = [9,3,9,6,0,1]

state = [3, 7]

elf1i = 0
elf2i = 1

#while len(state) < (in_num + 10):
# Could have added 1 or 2 digits, so both of these need to be checked
while state[-len(in_num):] != in_num and state[-(len(in_num)+1):-1] != in_num:
    elf1r = state[elf1i]
    elf2r = state[elf2i]

    next_recipe = elf1r + elf2r
    state.extend(divmod(next_recipe, 10) if next_recipe >= 10 else (next_recipe, ))

    elf1i = (elf1i + elf1r + 1) % len(state)
    elf2i = (elf2i + elf2r + 1) % len(state)
# end while

if state[-len(in_num):] == in_num:
    print(len(state) - len(in_num))
else:
    print(len(state) - len(in_num) - 1)
# end if

