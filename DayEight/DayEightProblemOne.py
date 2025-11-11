with open('input.txt', 'r') as input_file:
    city_map = [line.strip() for line in input_file]

height = len(city_map)
width = len(city_map[0])

antenna_dict = {}
for y in range(height):
    for x in range(width):
        antenna_value = city_map[y][x]
        if antenna_value != '.':
            antenna_dict.setdefault(antenna_value, []).append((x, y))

antinodes = set()
for antenna_type, antenna_positions in antenna_dict.items():
    if len(antenna_positions) > 1:
        for i in range(len(antenna_positions)):
            x1, y1 = antenna_positions[i]
            for j in range(i + 1, len(antenna_positions)):
                x2, y2 = antenna_positions[j]
                x_difference = x2 - x1
                y_difference = y2 - y1
                
                upper_x, upper_y = x1 - x_difference, y1 - y_difference
                lower_x, lower_y = x2 + x_difference, y2 + y_difference

                if 0 <= upper_x < width and 0 <= upper_y < height:
                    antinodes.add((upper_x, upper_y))
                if 0 <= lower_x < width and 0 <= lower_y < height:
                    antinodes.add((lower_x, lower_y))

print(len(antinodes))
                        