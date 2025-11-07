from enum import Enum, auto

with open('input.txt', 'r') as guard_map_file:
    guard_map = [line.strip() for line in guard_map_file]

for x in range(len(guard_map)):
    for y in range(len(guard_map[0])):
        if guard_map[x][y] == "^":
            #For ease of use input just says guard is facing north.  Might need to parse the direction normally
            guard_starting_position = (x, y)
    
class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def turn_right(self):
        return {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }[self]

    def move_forward_vector(self):
        return {
            Direction.NORTH: (-1, 0),
            Direction.EAST: (0, 1),
            Direction.SOUTH: (1, 0),
            Direction.WEST: (0, -1),
        }[self]


visited_points = set()
current_point = guard_starting_position
current_direction = Direction.NORTH

while True:
    visited_points.add(current_point)
    move_forward_vector = current_direction.move_forward_vector()
    next_point = (current_point[0] + move_forward_vector[0], current_point[1] + move_forward_vector[1])

    if next_point[0] < 0 or next_point[0] >= len(guard_map) or next_point[1] < 0 or next_point[1] >= len(guard_map[0]):
        break

    if guard_map[next_point[0]][next_point[1]] == "#":
        current_direction = current_direction.turn_right()
    else:
        current_point = next_point

print(len(visited_points))

    
