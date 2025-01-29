"""Safety protocols require that new pages for safety manuals be printed in a specific order. 
The notation X|Y means that if page X and page Y are both part of an update, page X must be printed 
before page Y. You have both the page ordering rules and the pages to be produced in each update.

Puzzle input: The first section lists the page ordering rules, and the second section lists the pages 
for each update. For example, the rule 47|53 means that if both pages 47 and 53 are in an update, 
page 47 must be printed before page 53.

Your task is to determine which updates are in the correct order according to the rules. 
Then, calculate the sum of the middle page numbers from those correctly ordered updates."""

def update_accepted(rules: list[list[str]], update: str) -> bool:
    """
    Checks if the update follows all the rules.
    
    Parameters:
    rules (list[list[str]]): The list of rules.
    update (str): The update to check.
    
    Returns:
    bool: True if the update is accepted, False otherwise.
    """
    update_list = update.split(",")  # Ensure the update is a list of strings
    for rule in rules:
        if rule[0] in update_list and rule[1] in update_list:
            if update_list.index(rule[0]) > update_list.index(rule[1]):
                return False
    return True

def find_middle_value(update: str) -> int:
    """
    Finds the middle value of the update.
    
    Parameters:
    update (str): The update to process.
    
    Returns:
    int: The middle value of the update.
    """
    update_list = update.split(",")
    middle_index = (len(update_list) - 1) // 2
    return int(update_list[middle_index])

# Initialize variables
rules = []
updates = []
count = 0

# Main logic
with open('day5.txt', 'r') as file:
    reading_rules = True
    for line in file:
        if not line.strip():
            reading_rules = False
            continue
        if reading_rules:
            rules.append(line.strip().split("|"))
        else:
            updates.append(line.strip())

# Process updates
for update in updates:
    if update_accepted(rules, update):
        middle_value = find_middle_value(update)
        count += middle_value

print(count)