import re
from pathlib import Path

#Silly one liner for the fun of it
print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", Path('input.txt').read_text())))