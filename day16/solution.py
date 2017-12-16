def parse_input(file_name):
    return [x.strip().split(',') for x in open(file_name).readlines()][0]


def spin(programs, operands):
    selected = list(reversed([programs.pop() for _ in range(int(operands[0]))]))
    selected.extend(programs)
    return selected


def exchange(programs, index_a, index_b):
    partner_a = programs[index_a]
    partner_b = programs[index_b]
    programs[index_a] = partner_b
    programs[index_b] = partner_a
    return programs


def index_exchange(programs, operands):
    return exchange(programs=programs, index_a=int(operands[0]), index_b=int(operands[1]))


def partner_exchange(programs, operands):
    return exchange(programs=programs, index_a=programs.index(operands[0]), index_b=programs.index(operands[1]))


def solve_part_one(programs, instructions):
    operations = {'x': index_exchange, 'p': partner_exchange, 's': spin}
    for instruction in instructions:
        programs = operations.get(instruction[0])(programs, instruction[1:].split('/'))
    return ''.join(programs)


initial_programs = [chr(x) for x in range(ord('a'), ord('p') + 1)]
print(solve_part_one(initial_programs, parse_input('input')))
