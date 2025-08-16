def is_monotonic(level):
    return level == sorted(level) or level == sorted(level, reverse=True)

def is_difference_acceptable(level):
    return all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))

with open('input.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()
levels = [list(map(int, line.split())) for line in lines]

valid_levels_count = sum(1 for line in levels if is_monotonic(line) and is_difference_acceptable(line))
print(valid_levels_count)