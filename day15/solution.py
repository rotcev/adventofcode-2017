def parse_seeds(file_input):
    return tuple([int(x.split('with ')[1]) for x in open(file_input).readlines()])


def generate_next(previous, factor, divisor=None):
    next_value = (previous * factor) % 2147483647
    if divisor is None:
        return next_value
    if next_value % divisor == 0:
        return next_value
    while next_value % divisor != 0:
        next_value = generate_next(next_value, factor, divisor=None)
    return next_value


def generator_a(seed, divisor=None):
    return generate_next(seed, 16807, divisor)


def generator_b(seed, divisor=None):
    return generate_next(seed, 48271, divisor)


def solve(seed_a, seed_b, iterations, divisor_a=None, divisor_b=None):
    gen_a = generator_a(seed_a, divisor=divisor_a)
    gen_b = generator_b(seed_b, divisor=divisor_b)
    judge_count = 0
    for i in range(iterations):
        low_a = gen_a & 0xFFFF
        low_b = gen_b & 0xFFFF
        if low_a == low_b:
            judge_count += 1
        gen_a = generator_a(gen_a, divisor=divisor_a)
        gen_b = generator_b(gen_b, divisor=divisor_b)
    return judge_count


seed_a, seed_b = parse_seeds('input')
print(solve(seed_a, seed_b, 40000000))
print(solve(seed_a, seed_b, 5000000, divisor_a=4, divisor_b=8))
