def parse_input(file_name):
    return [int(x.rstrip()) for x in open(file_name).readlines()]


def solve(data, jump_function):
    maze_length = len(data)
    pointer = 0
    steps = 0
    while 0 <= pointer < maze_length:
        increment = data[pointer]
        data[pointer] += jump_function(increment)
        pointer += increment
        steps += 1
    return steps


print(solve(parse_input('input'), lambda x: 1))
print(solve(parse_input('input'), lambda x: 1 if x < 3 else -1))
