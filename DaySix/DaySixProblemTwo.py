from enum import Enum, auto
import copy

with open('input.txt', 'r') as guard_map_file:
    guard_map = [list(line.strip()) for line in guard_map_file]


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

def map_navigation_has_loops(mutated_guard_map):
    visited_points = set()
    current_point = guard_starting_position
    current_direction = Direction.NORTH

    while True:
        coordinates = (current_point, current_direction)
        if coordinates in visited_points:
            #If we've already hit this point from the same direction previously it's a loop
            return True, visited_points
        
        visited_points.add(coordinates)
        move_forward_vector = current_direction.move_forward_vector()
        next_point = (current_point[0] + move_forward_vector[0], current_point[1] + move_forward_vector[1])

        if next_point[0] < 0 or next_point[0] >= len(mutated_guard_map) or next_point[1] < 0 or next_point[1] >= len(mutated_guard_map[0]):
            break

        if mutated_guard_map[next_point[0]][next_point[1]] == "#" or mutated_guard_map[next_point[0]][next_point[1]] == "0":
            current_direction = current_direction.turn_right()
        else:
            current_point = next_point

    return False, visited_points

#Test the initial path without changing anything.  All obstructions will have to be on this path
has_loops, initial_visited_path = map_navigation_has_loops(guard_map)

obstruction_count = 0
# Only test each grid coordinate once. initial_visited_path contains (position, direction)
unique_positions = {coords for (coords, _dir) in initial_visited_path}
for point_coordinates in unique_positions:
    copied_guard_map = copy.deepcopy(guard_map)
    copied_guard_map[point_coordinates[0]][point_coordinates[1]] = '0'

    mutation_has_loops, mutation_visited_paths = map_navigation_has_loops(copied_guard_map)
    if mutation_has_loops:
        obstruction_count += 1

print(obstruction_count)


    
