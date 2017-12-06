def parse_input(file_name):
    return list(map(lambda z: list(map(int, z.split(' '))),
                    [x for x in [y.strip().replace('\t', ' ') for y in open(file_name).readlines()]]))


def solution_one(data):
    return sum([a - b for (a, b) in zip(map(max, data), map(min, data))])


def solution_two(data):
    def divide_row(row):
        for x in range(len(row)):
            for y in range(len(row)):
                if row[y] == row[x]:
                    continue
                if row[x] % row[y] == 0:
                    return row[x] // row[y]
        return 0

    return sum(map(divide_row, data))


file_input = parse_input('input')
print(solution_one(file_input))
print(solution_two(file_input))
