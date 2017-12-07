def parse_input(file_name):
    return list(map(int, open(file_name).readline()))


def solve(data):
    sum = 0
    for i in range(len(data)):
        curr = data[i]
        next = data[i + 1 if i + 1 < len(data) else -1]
        if curr == next:
            sum += curr
    return sum


file_input = parse_input('input')
print(file_input)
print(solve(file_input))
