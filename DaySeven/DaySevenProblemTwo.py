with open('input.txt', 'r') as calibration_file:
    calibrations = [line.strip() for line in calibration_file]

def permutation_total_matches(goal, calculations, total, totals):
    if not calculations:
        if total == goal:
            totals.append(total)
    elif total < goal:
        permutation_total_matches(goal, calculations[1:], total + calculations[0], totals)
        permutation_total_matches(goal, calculations[1:], calculations[0] if total == 0 else calculations[0] * total, totals)
        permutation_total_matches(goal, calculations[1:], calculations[0] if total == 0 else int(str(total) + str(calculations[0])), totals)

sum_goals = 0
for calibration in calibrations:
    split_calibration = calibration.split(": ")
    goal = int(split_calibration[0])
    calculations = [int(calculation) for calculation in split_calibration[1].split(" ")]
    permutations = []
    permutation_total_matches(goal, calculations, 0, permutations)
    if permutations:
        sum_goals += goal

print(sum_goals)