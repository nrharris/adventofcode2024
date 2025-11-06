def increment_count_if_matches(snippet):
    if "XMAS" == snippet or "SAMX" == snippet:
        return 1
    return 0

with open('input.txt', 'r') as file:
    all_lines = [line.strip() for line in file]

count = 0
row_length = len(all_lines)
column_length = len(all_lines[0])
for row in range(row_length):
    for column in range(column_length):
        if row + 3 < row_length:
            #Vertical match
            count += increment_count_if_matches(all_lines[row][column] + all_lines[row+1][column] + all_lines[row+2][column] + all_lines[row+3][column])
        if column + 3 < column_length:
            #Horizontala match
            count += increment_count_if_matches(all_lines[row][column] + all_lines[row][column+1] + all_lines[row][column+2] + all_lines[row][column+3])
        if row + 3 < row_length and column + 3 < column_length:
            #Diagonal down-right match
            count += increment_count_if_matches(all_lines[row][column] + all_lines[row+1][column+1] + all_lines[row+2][column+2] + all_lines[row+3][column+3])
        if row + 3 < row_length and column - 3 >= 0:
            #Diagonal down-left match
            count += increment_count_if_matches(all_lines[row][column] + all_lines[row+1][column-1] + all_lines[row+2][column-2] + all_lines[row+3][column-3])

print(count)
        