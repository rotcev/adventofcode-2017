from itertools import permutations


def parse_input(file_name):
    return [x.rstrip().split(' ') for x in open(file_name).readlines()]


def permute_string(value):
    return [''.join(x) for x in permutations(value, len(value))]


def is_valid_passphrase_solution_one(passphrase):
    words = set()
    for word in passphrase:
        if word in words:
            return False
        words.add(word)
    return True


def is_valid_passphrase_solution_two(passphrase):
    if not is_valid_passphrase_solution_one(passphrase):
        return False
    for word in passphrase:
        if any(x in passphrase for x in filter(lambda y: y != word, permute_string(word))):
            return False
    return True


def solve(data, validation_function):
    return sum(map(lambda x: 1 if validation_function(x) else 0, data))


print(solve(parse_input('input'), is_valid_passphrase_solution_one))
print(solve(parse_input('input'), is_valid_passphrase_solution_two))
