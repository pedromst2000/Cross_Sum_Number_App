from tkinter import messagebox, Entry
from app.utils.validations import (
    validate_input,
    calculate_cross_sum,
)


def show_message(message: messagebox, input_val: Entry) -> None:
    """
    Displays a message box with the given message.

    Args:
        message (messagebox): The messagebox module to use for displaying messages.
        input_val (Entry): The input value to validate and display.

    Returns:
        None
    """
    if not validate_input(input_val):
        message.showerror("Error", "Please enter a valid number.")
    else:
        message.showinfo("Result", f"{calculate_cross_sum(input_val)}")


def display_opening_message():
    """
    Display an opening message in the Tkinter window.

    Returns:
        None
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

    Returns:
        None
    """
    show_message(messagebox, entry_widget.get())
