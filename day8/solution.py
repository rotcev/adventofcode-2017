import operator


def parse_input(file_name):
    return [x.strip().split(' if ') for x in open(file_name).readlines()]


def parse_statements(data):
    register_names = {}
    conditions = []
    operations = []
    for fst, lst in data:
        operation = fst.split()
        condition = lst.split()
        condition[2] = int(condition[2])
        operation[2] = int(operation[2])
        register_names[operation[0]] = 0
        operations.append(operation)
        conditions.append(condition)
    return register_names, operations, conditions


def evaluate_conditions(registers, operations, conditions):
    max_register_value = 0
    for x in range(len(conditions)):
        condition = conditions[x]
        if evaluate_condition(registers[condition[0]], condition[1], condition[2]):
            op = operations[x]
            op_register_name = op[0]
            function = op[1]
            op_operand = op[2]
            if function == 'inc':
                registers[op_register_name] += op_operand
            elif function == 'dec':
                registers[op_register_name] -= op_operand
            if registers[op_register_name] > max_register_value:
                max_register_value = registers[op_register_name]

    return registers, max_register_value


condition_operators = {'>': operator.gt, '<': operator.lt, '<=': operator.le, '>=': operator.ge, '!=': operator.ne,
                       '==': operator.eq}


def evaluate_condition(condition_register, condition_operator, condition_operand):
    return condition_operators[condition_operator](condition_register, condition_operand)


registers, operations, conditions = parse_statements(parse_input('input'))
evaluated, max_register_value = evaluate_conditions(registers, operations, conditions)
print(registers[max(evaluated, key=evaluated.get)])
print(max_register_value)
