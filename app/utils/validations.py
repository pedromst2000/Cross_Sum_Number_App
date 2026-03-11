from tkinter import Entry


def validate_input(input_string: Entry) -> bool:
    """
    Validates the input string to ensure it contains only digits and is not empty.

    Args:
        input_string (Entry): Entry widget containing the input string.

    Returns:
        bool: True if the input is valid (non-empty and contains only digits), False otherwise.
    """
    if not input_string or not input_string.isdigit():
        return False
    return True


def calculate_cross_sum(input_val: str) -> int:
    """
    Calculates the cross sum of the given input value.

    Args:
        input_val (str): The input value as a string.

    Returns:
        int: The cross sum of the digits in the input value.
    """
    return sum(int(digit) for digit in input_val if digit.isdigit())
