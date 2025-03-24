import sys
import numpy as np
from itertools import product

def evaluate_left_to_right(numbers, operators):
    """Evaluate the expression strictly left-to-right using the given numbers and operators."""
    result = numbers[0]
    try:
        for op, num in zip(operators, numbers[1:]):
            if op == '+':
                result += num
            elif op == '*':
                result *= num
            # Check if result overflows and break early
            if result > sys.maxsize:  # sys.maxsize is the largest integer the system can handle
                return None
    except OverflowError:
        return None  # Return None if overflow occurs
    return result

def equation_is_valid(target, numbers):
    """
    Return True if there exists an insertion of '+' or '*'
    between the numbers that evaluates to the target.
    """
    # Generate all possible operator combinations
    for ops in product("+" "*", repeat=len(numbers)-1):
        result = evaluate_left_to_right(numbers, ops)
        if result == target:
            return True
    return False

def main():
    valid_sum = 0
    try:
        with open("input/day7.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                # Split input into target value and numbers
                target_str, numbers_str = line.split(':')
                target = int(target_str.strip())
                numbers = [int(x) for x in numbers_str.split()]
                if equation_is_valid(target, numbers):
                    valid_sum += target
        print(valid_sum)
    except FileNotFoundError:
        print("The file 'input/day7.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
