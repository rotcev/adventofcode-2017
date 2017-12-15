import operator
from copy import deepcopy


def safe_index_of(data, value):
    try:
        return data.index(value)
    except ValueError:
        return None


def initialize_firewall(file_name):
    firewall = {}

    def initialize_ranges(range_length, default_value):
        depths = [0] * int(range_length)
        depths[0] = default_value
        return depths

    for line in [x.split(': ') for x in open(file_name).readlines()]:
        firewall[int(line[0])] = initialize_ranges(int(line[1]), 1)
    max_key = max(firewall.items(), key=operator.itemgetter(0))[0]
    for x in range(max_key):
        if x not in firewall:
            firewall[x] = initialize_ranges(1, 0)
    directions = [1] * len(firewall)
    return firewall, directions


def get_next_scanner_index(current_scanner_index, current_depth, ranges, directions):
    next_scanner_index = current_scanner_index + directions[current_depth]
    if next_scanner_index >= len(ranges):
        directions[current_depth] = -1
        next_scanner_index = current_scanner_index - 1

    if next_scanner_index < 0:
        directions[current_depth] = 1
        next_scanner_index = 1
    return next_scanner_index


def move_scanners(current_firewall, directions):
    updated_firewall = deepcopy(current_firewall)
    for depth, ranges in current_firewall.items():
        current_scanner_index = safe_index_of(ranges, 1)
        if current_scanner_index is None:
            continue
        ranges[current_scanner_index] = 0
        ranges[get_next_scanner_index(current_scanner_index, depth, ranges, directions)] = 1
        updated_firewall[depth] = ranges
    return updated_firewall


def solve_part_one(firewall, directions):
    packet_layer = 0
    severity = 0
    for i in range(len(firewall)):
        current_scanner_position = safe_index_of(firewall[packet_layer], 1)

        if current_scanner_position == 0:
            severity += packet_layer * len(firewall[packet_layer])

        firewall = move_scanners(firewall, directions)
        print('{}, {}'.format(packet_layer, firewall))
        packet_layer += 1
    return severity


initial_firewall, initial_directions = initialize_firewall('input')
print(solve_part_one(initial_firewall, initial_directions))
