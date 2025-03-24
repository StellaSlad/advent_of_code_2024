""" Problem description:

Input example:
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

Each line in the input represents a single equation. The test value appears before the colon on each line; 
it is your job to determine whether the remaining numbers can be combined with mathematical operators ("+" or "*") to produce the test value.
Operators are always evaluated left-to-right, not according to precedence rules; numbers in the equations cannot be rearranged. 
The puzzle answer is the sum of the values of all the equations that could possibly be true."""

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
