from typing import Any, Union

from tkinter import messagebox, Entry
from app.utils.validations import validate_input, calculate_cross_sum, _extract_value


def show_message(message: Any, input_val: Union[str, Entry, None]) -> None:
    """
    Displays a message box with the given message.

    Accepts either a plain string or an Entry-like object for `input_val`.

    Parameters:
        message: The message box module (e.g., tkinter.messagebox) to use for displaying
                    messages.
        input_val: The input value to validate and calculate the cross sum for. Can be a string,
                    an Entry-like object, or None.
    Returns:
        None
    """
    # Normalize value (works for str, Entry-like objects, or None)
    val = _extract_value(input_val)

    if not validate_input(val):
        message.showerror("Error", "Please enter a valid number.")
    else:
        message.showinfo("Result", f"{calculate_cross_sum(val)}")


def display_opening_message():
    """
    Display an opening message in the Tkinter window.
    """
    messagebox.showinfo(
        "Welcome",
        "Welcome to the Cross Sum Number application!\n"
        "A cross sum is the sum of all digits in a number.\n"
        "For example, the cross sum of 12345 is 1 + 2 + 3 + 4 + 5 = 15.\n",
    )


def handle_calculate(entry_widget) -> None:
    """
    Handle the calculate button click event.

    Args:
        entry_widget: The Entry-like widget to get the input from.
    """

    # Pass the Entry widget itself; show_message will extract its value safely
    show_message(messagebox, entry_widget)
