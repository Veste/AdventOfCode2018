import part1
import ast

samples_p = []

with open('input') as sample_f:
    samples = sample_f.readlines()
    for i in range(0, len(samples), 4):
        sample = samples[i:i + 3]
        before = ast.literal_eval(sample[0][8:-1])
        results = [int(i) for i in sample[1].strip().split()]
        after = ast.literal_eval(sample[2][8:])
        samples_p.append((before, results, after))
# end with

op_list = [
    part1.addr,
    part1.addi,
    part1.mulr,
    part1.muli,
    part1.banr,
    part1.bani,
    part1.borr,
    part1.bori,
    part1.setr,
    part1.seti,
    part1.gtir,
    part1.gtri,
    part1.gtrr,
    part1.eqir,
    part1.eqri,
    part1.eqrr
]

opcode_map = {}

for s in samples_p:
    before = s[0]
    after = s[2]
    print("{}  to  {} w/ inputs {}".format(before, after, s[1][1:]))
    passing_ops = []
    for op in op_list:
        op_result = op(before[:], s[1][1], s[1][2], s[1][3])
        print("{} {} {}".format(before, op.__name__, op_result))
        if op_result == after:
            passing_ops.append(op)
    # end for
    print()

    for opcode in passing_ops:
        if s[1][0] in opcode_map:
            opcode_map[s[1][0]].add(opcode)
        else:
            opcode_map[s[1][0]] = {[opcode]}
        # end if
    # end for
# end for

matched_opcodes = {k: None for k in opcode_map.keys()}
while None in matched_opcodes.values():
    for k in opcode_map.keys():
        opcode_options = opcode_map[k]
        filtered_opts = [opt for opt in opcode_options if opt not in matched_opcodes.values()]
        if len(filtered_opts) == 1:
            matched_opcodes[k] = filtered_opts[0]
        # end if
    # end for
# end while

for k, v in sorted(matched_opcodes.items(), key=lambda x: x[1].__name__):
    print(k, v.__name__)

# Now run the program
program_lines = []
with open('input_program') as inpf:
    for pl in inpf:
        program_lines.append([int(i) for i in pl.strip().split()])
# end with

program_registers = [0, 0, 0, 0]
for program_line in program_lines:
    op = matched_opcodes[program_line[0]]
    op(program_registers, program_line[1], program_line[2], program_line[3])
# end for

print()
print(program_registers)

