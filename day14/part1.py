in_num = 9 # 5158916779
in_num = 5 # 0124515891
in_num = 18 # 9251071085
in_num = 2018 # 5941429882
in_num = 939601

state = [3, 7]

elf1i = 0
elf2i = 1

while len(state) < (in_num + 10):
    elf1r = state[elf1i]
    elf2r = state[elf2i]

    next_recipe = elf1r + elf2r
    state.extend(divmod(next_recipe, 10) if next_recipe >= 10 else (next_recipe, ))

    if len(state) % 10000 == 0:
        print(state[::-1])

    elf1i = (elf1i + elf1r + 1) % len(state)
    elf2i = (elf2i + elf2r + 1) % len(state)
# end while

print("".join(str(s) for s in state[in_num:in_num+10]))

