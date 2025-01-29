"""The puzzle input consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?"""

def check(arr: list[int]) -> bool:
    """
    This function checks if the levels in the array are either 
    gradually increasing or gradually decreasing, and that any 
    two adjacent levels differ by at least one and at most three.
    
    Parameters:
    arr (list[int]): The list of levels.
    
    Returns:
    bool: True if the levels are safe, False otherwise.
    """
    diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    return (all(x > 0 for x in diff) or all(x < 0 for x in diff)) and all(1 <= abs(x) <= 3 for x in diff)


count = 0

with open('input/day2.txt', 'r') as file:
    for line in file:
        elements = line.split()
        levels = list(map(int, elements))
        # Check if this line is safe
        if check(levels):
            count += 1

print(count)