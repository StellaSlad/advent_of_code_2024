""" Task description Day 1:

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: 
their list of locations to check is currently empty. Eventually, someone decides that the best 
place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. 
Instead, the Elves discover an assortment of notes and lists of historically significant locations! This 
seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used 
to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by 
a unique number called the location ID. To make sure they don't miss anything, The Historians split 
into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly 
becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?
To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in 
the left list with the smallest number in the right list, then the second-smallest left number with 
the second-smallest right number, and so on. Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
What is the total distance between your lists?"""

# Open the file and read the contents
col1 = []
col2 = []
with open('input_day1.txt', 'r') as file:
    for line in file:
        elements = line.split()
        col1.append(int(elements[0]))
        col2.append(int(elements[1]))

# Sort the numbers in ascending order
col1_sorted = sorted(col1)
col2_sorted = sorted(col2)

# Calculate and print the total distance
total_distance = sum(abs(a - b) for a, b in zip(col1_sorted, col2_sorted))
print(total_distance)
