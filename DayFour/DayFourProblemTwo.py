with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

count = 0
row_length = len(lines)
column_length = len(lines[0])
for row in range(row_length):
    for col in range(column_length):
        if lines[row][col] == 'A':
            if 0 < row < row_length-1 and 0 < col < column_length-1:
                uppper_left_to_lower_right_diag = lines[row-1][col-1] + lines[row+1][col+1]
                lower_left_to_upper_right_diag = lines[row+1][col-1] + lines[row-1][col+1]
                descending_diagonal_matches = uppper_left_to_lower_right_diag == "SM" or uppper_left_to_lower_right_diag == "MS"
                ascending_diagonal_matches = lower_left_to_upper_right_diag == "SM" or lower_left_to_upper_right_diag == "MS"
                if descending_diagonal_matches and ascending_diagonal_matches:
                    count += 1

print(count)
                