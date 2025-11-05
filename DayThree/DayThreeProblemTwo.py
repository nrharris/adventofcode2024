import re
from pathlib import Path

pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
with open('input.txt', 'r') as file:
    input = file.read()

sum = 0
enabled = True
for match in pattern.finditer(input):
    if match.group(4):
        enabled = False
    elif match.group(3):
        enabled = True
    elif enabled:
        sum += int(match.group(1)) * int(match.group(2))

print(sum)
        
                          