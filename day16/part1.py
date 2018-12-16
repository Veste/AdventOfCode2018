import ast


def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]
    return registers
# end addr


def addi(registers, a, b, c):
    registers[c] = registers[a] + b
    return registers
# end addi


def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]
    return registers
# end addr


def muli(registers, a, b, c):
    registers[c] = registers[a] * b
    return registers
# end addr


def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]
    return registers
# end addr


def bani(registers, a, b, c):
    registers[c] = registers[a] & b
    return registers
# end addr


def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]
    return registers
# end addr


def bori(registers, a, b, c):
    registers[c] = registers[a] | b
    return registers
# end addr


def setr(registers, a, b, c):
    registers[c] = registers[a]
    return registers
# end addr


def seti(registers, a, b, c):
    registers[c] = a
    return registers
# end addr


def gtir(registers, a, b, c):
    registers[c] = 1 if a > registers[b] else 0
    return registers
# end addr


def gtri(registers, a, b, c):
    registers[c] = 1 if registers[a] > b else 0
    return registers
# end addr


def gtrr(registers, a, b, c):
    registers[c] = 1 if registers[a] > registers[b] else 0
    return registers
# end addr


def eqir(registers, a, b, c):
    registers[c] = 1 if a == registers[b] else 0
    return registers
# end addr


def eqri(registers, a, b, c):
    registers[c] = 1 if registers[a] == b else 0
    return registers
# end addr


def eqrr(registers, a, b, c):
    registers[c] = 1 if registers[a] == registers[b] else 0
    return registers
# end addr


if __name__ == "__main__":
    samples_p = []

    with open('input') as sample_f:
        samples = sample_f.readlines()
        for i in range(0, len(samples), 4):
            sample = samples[i:i+3]
            before = ast.literal_eval(sample[0][8:-1])
            results = [int(i) for i in sample[1].strip().split()]
            after = ast.literal_eval(sample[2][8:])
            samples_p.append((before, results, after))
    # end with

    op_list = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    ngsamples = 0
    for s in samples_p:
        ngops = 0
        before = s[0]
        after = s[2]
        print("{}  to  {} w/ inputs {}".format(before, after, s[1][1:]))
        for op in op_list:
            op_result = op(before[:], s[1][1], s[1][2], s[1][3])
            print("{} {} {}".format(before, op.__name__, op_result))
            if op_result == after:
                ngops += 1
        # end for
        print()
        if ngops > 2:
            print("Successful sample")
            ngsamples += 1
    # end for

    print(ngsamples)

