from tkinter import Entry
from typing import Optional, Union


def _extract_value(value: Union[str, Entry, None]) -> Optional[str]:
    """
    Helper function to extract a string value from various input types.

    Args:
        value: The input value which can be a string, an Entry-like object, or None
    Returns:
        Optional[str]: The extracted string value if possible, or None if the input is None.
    """

    if value is None:
        return None
    # If it's an Entry widget, extract its text
    if isinstance(value, Entry):
        return value.get()
    # If it looks like an Entry-like (duck-typed) object with a callable get(), use it
    if hasattr(value, "get") and callable(getattr(value, "get")):
        maybe = value.get()
        if isinstance(maybe, str):
            return maybe
        # Coerce other types to string representation
        return str(maybe)
    # If it's already a string, return as-is
    if isinstance(value, str):
        return value
    # Unknown type -> treat as None (defensive fallback, not reachable via public API)
    return None  # pragma: no cover


def validate_input(input_value: Union[str, Entry, None]) -> bool:
    """
    Validates the input value to ensure it is a non-empty string containing only digits.

    Accepts None, a string, or an Entry-like object and checks if the resulting string is valid.

    Args:
        input_value: The input value to validate, which can be a string, an Entry-like object, or None.
    Returns:
        bool: True if the input is valid (non-empty and contains only digits), False otherwise.
    """
    val = _extract_value(input_value)
    if not isinstance(val, str):
        return False
    if not val or not val.isdigit():
        return False
    return True


def calculate_cross_sum(input_val: Optional[str]) -> int:
    """
    Calculates the cross sum of the given input value.

    Accepts None or a string and sums any digit characters found.

    Args:
        input_val: The input value to calculate the cross sum for. Can be a string or None.
    Returns:
        int: The calculated cross sum of the digits in the input value.
    """
    if input_val is None:
        return 0
    return sum(int(digit) for digit in input_val if digit.isdigit())
