from collections import defaultdict
import functools

#Reading in input
with open('pageordering.txt', 'r') as page_ordering_file:
    page_ordering_pairs = [line.strip().split("|") for line in page_ordering_file]

page_ordering_dict = defaultdict(list)
for page_ordering_pair in page_ordering_pairs:
    key = page_ordering_pair[0]
    value = page_ordering_pair[1]
    page_ordering_dict[key].append(value)

with open('pages.txt', 'r') as page_file:
    page_lists = [line.strip().split(",") for line in page_file]

#Actual functionality.  Note: Wouldn't work if there was cycle
def compare_pages(page_one, page_two):
    if page_one in page_ordering_dict and page_two in page_ordering_dict[page_one]:
        return -1
    elif page_two in page_ordering_dict and page_one in page_ordering_dict[page_two]:
        return 1
    else:
        return 0
    
sum = 0   
for pages in page_lists:
    sorted_pages = sorted(pages, key=functools.cmp_to_key(compare_pages))
    #The only difference between problem one and problem two is a != here for day 2
    if sorted_pages == pages:
        sum += int(sorted_pages[len(sorted_pages) // 2])

print(sum)