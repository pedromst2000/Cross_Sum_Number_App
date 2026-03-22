import tkinter

from hypothesis import given, strategies as st

from app.utils.validations import validate_input, calculate_cross_sum
from app.utils.events import show_message, display_opening_message, handle_calculate

# ----------------------------- validate_input tests -----------------------------


def test_validate_input_valid_number():
    """Test that validate_input returns True for a valid number input."""
    assert validate_input("12345")


def test_validate_input_empty():
    """Test that validate_input returns False for empty input."""
    assert not validate_input("")


def test_validate_input_invalid_non_digit():
    """Test that validate_input returns False for a mixed alphanumeric input."""
    assert not validate_input("12a34")


def test_validate_input_whitespace():
    """Test that validate_input returns False for whitespace-only input."""
    assert not validate_input("   ")


def test_validate_input_single_digit():
    """Test that validate_input returns True for a single digit."""
    assert validate_input("7")


def test_validate_input_whitespace_wrapped():
    """
    Test that validate_input returns False for input with leading/trailing whitespace.
    """

    assert not validate_input(" 123 ")


def test_validate_input_signed_number():
    """
    Test that validate_input returns False for signed numbers.
    """

    assert not validate_input("-123")


def test_validate_input_decimal_number():
    """
    Test that validate_input returns False for decimal numbers.
    """
    assert not validate_input("12.3")


def test_validate_input_none():
    """
    Test that validate_input returns False for None input.
    """
    assert not validate_input(None)


# ----------------------------- calculate_cross_sum tests -----------------------------


def test_calculate_cross_sum_basic():
    """Test that calculate_cross_sum returns the correct sum of digits.

    Asserts:
        - calculate_cross_sum("12345") == 15
    """
    assert calculate_cross_sum("12345") == 15


def test_calculate_cross_sum_with_zeros():
    """Test that calculate_cross_sum correctly handles all-zero input.

    Asserts:
        - calculate_cross_sum("0000") == 0
    """
    assert calculate_cross_sum("0000") == 0


def test_calculate_cross_sum_with_non_digits():
    """Test that calculate_cross_sum ignores non-digit characters.

    Asserts:
        - calculate_cross_sum("12a3b4") == 10
    """
    assert calculate_cross_sum("12a3b4") == 10


def test_calculate_cross_sum_single_digit():
    """Test that calculate_cross_sum works correctly for a single digit.

    Asserts:
        - calculate_cross_sum("7") == 7
    """
    assert calculate_cross_sum("7") == 7


def test_calculate_cross_sum_large_number():
    """Test that calculate_cross_sum handles a large number correctly.

    Asserts:
        - calculate_cross_sum("99999") == 45
    """
    assert calculate_cross_sum("99999") == 45


def test_calculate_cross_sum_decimal_and_negative():
    """
    Test that calculate_cross_sum correctly sums digits in a string with decimal and negative signs.

    Asserts:
        - calculate_cross_sum("12.3") == 6
        - calculate_cross_sum("-123") == 6
    """

    assert calculate_cross_sum("12.3") == 6
    assert calculate_cross_sum("-123") == 6


# ----------------------------- show_message tests -----------------------------


def test_show_message_valid(mocker):
    """Test that show_message calls showinfo with the correct parameters for valid input.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showinfo is called with ("Result", "6")
    """
    mock_showinfo = mocker.patch("tkinter.messagebox.showinfo")
    show_message(tkinter.messagebox, "123")
    mock_showinfo.assert_called_with("Result", "6")


def test_show_message_invalid_empty(mocker):
    """Test that show_message calls showerror for empty input.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showerror is called with ("Error", "Please enter a valid number.")
    """
    mock_showerror = mocker.patch("tkinter.messagebox.showerror")
    show_message(tkinter.messagebox, "")
    mock_showerror.assert_called_with("Error", "Please enter a valid number.")


def test_show_message_invalid_nondigit(mocker):
    """Test that show_message calls showerror for non-digit input.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showerror is called with ("Error", "Please enter a valid number.")
    """
    mock_showerror = mocker.patch("tkinter.messagebox.showerror")
    show_message(tkinter.messagebox, "12a")
    mock_showerror.assert_called_with("Error", "Please enter a valid number.")


# ----------------------------- display_opening_message tests -----------------------------


def test_display_opening_message(mocker):
    """Test that display_opening_message calls showinfo with the Welcome message.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showinfo is called once with ("Welcome", ...) containing the app intro text.
    """
    mock_showinfo = mocker.patch("tkinter.messagebox.showinfo")
    display_opening_message()
    mock_showinfo.assert_called_once_with(
        "Welcome",
        "Welcome to the Cross Sum Number application!\n"
        "A cross sum is the sum of all digits in a number.\n"
        "For example, the cross sum of 12345 is 1 + 2 + 3 + 4 + 5 = 15.\n",
    )


# ----------------------------- handle_calculate tests -----------------------------


def test_handle_calculate_valid(mocker):
    """Test that handle_calculate calls showinfo with the result for valid input.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showinfo is called with ("Result", "6") for input "123".
    """
    mock_showinfo = mocker.patch("tkinter.messagebox.showinfo")
    mock_entry = mocker.MagicMock()
    mock_entry.get.return_value = "123"
    handle_calculate(mock_entry)
    mock_showinfo.assert_called_with("Result", "6")


def test_handle_calculate_invalid(mocker):
    """Test that handle_calculate calls showerror for invalid input.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showerror is called with ("Error", "Please enter a valid number.").
    """
    mock_showerror = mocker.patch("tkinter.messagebox.showerror")
    mock_entry = mocker.MagicMock()
    mock_entry.get.return_value = ""
    handle_calculate(mock_entry)
    mock_showerror.assert_called_with("Error", "Please enter a valid number.")


def test_handle_calculate_entry_get_returns_none(mocker):
    """
    Test that handle_calculate calls showerror if the Entry's get() method returns None.

    Args:
        mocker: pytest-mock fixture for patching tkinter.messagebox.

    Asserts:
        - messagebox.showerror is called with ("Error", "Please enter a valid number.
        ") when the Entry's get() method returns None.
    """

    mock_showerror = mocker.patch("tkinter.messagebox.showerror")
    mock_entry = mocker.MagicMock()
    mock_entry.get.return_value = None
    handle_calculate(mock_entry)
    mock_showerror.assert_called_with("Error", "Please enter a valid number.")


def test_calculate_cross_sum_none():
    """Test that calculate_cross_sum returns 0 when passed None."""
    assert calculate_cross_sum(None) == 0


# ----------------------------- property-based tests -----------------------------


@given(st.text())
def test_validate_input_with_various_strings(s):
    """Property: validate_input returns True only for non-empty all-digit strings."""
    if s.isdigit() and s != "":
        assert validate_input(s)
    else:
        assert not validate_input(s)


@given(st.integers(min_value=0, max_value=10**6))
def test_calculate_cross_sum_matches_naive(n):
    """Property: calculate_cross_sum equals the naive digit-sum for all non-negative integers."""
    s = str(n)
    expected = sum(int(ch) for ch in s if ch.isdigit())
    assert calculate_cross_sum(s) == expected
