from pathlib import Path
from typing import List

def read_in_lists(left_list, right_list):
    with Path('./input.txt').open('r') as f:
        for values in f.readlines():
            x = values.split('   ')
            left_list.append(int(x[0]))
            right_list.append(int(x[1]))

    left_list.sort()
    right_list.sort()

def print_absolute_list_difference(left_list, right_list):
    total_difference = 0
    for index, left_item in enumerate(left_list):
        difference = abs(left_item - right_list[index])
        total_difference += difference

    print(total_difference) 

def print_similarity_score(left_list, right_list):
    total_similiarity_score = 0
    unique_values = set(left_list)
    for item in unique_values:
        appearances = right_list.count(item)
        total_similiarity_score += item * appearances
    print(total_similiarity_score)

left_list = []
right_list = []

read_in_lists(left_list, right_list)
#PART ONE
print_absolute_list_difference(left_list, right_list)

#PART TWO
print_similarity_score(left_list, right_list)


   