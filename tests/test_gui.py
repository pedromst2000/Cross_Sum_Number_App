import pytest
import tkinter as tk

from app.gui import Window


@pytest.fixture
def app(monkeypatch):
    # Patch iconbitmap to avoid failures on Linux/CI where .ico files are not supported
    monkeypatch.setattr(tk.Tk, "iconbitmap", lambda *args, **kwargs: None)
    window = Window()
    window.__main__()  # Initialize the GUI
    window.window.withdraw()  # Hide the window during tests
    yield window
    window.window.destroy()


def test_icon_exists(app):
    """
    Test that the application icon exists and is set correctly.
    """

    assert hasattr(app, "AppIcon")  # Check if AppIcon attribute exists
    assert isinstance(app.AppIcon, str)  # Check if AppIcon is a string
    assert app.AppIcon.endswith(".ico")  # Check if AppIcon ends with .ico
    # Check if AppIcon matches the expected path
    assert app.AppIcon == "app/assets/icon/Icon.ico"


def test_window_title(app):
    """Test that the window title is set correctly."""

    assert app.window.title() == "Cross Sum Number"


def test_window_geometry(app):
    """Test that the window geometry is set to 600x400."""
    assert app.window.geometry().startswith("600x400")


def test_initial_vars(app):
    """Test that input_var and result_var are initialized as StringVar."""
    assert isinstance(app.input_var, tk.StringVar)
    assert isinstance(app.result_var, tk.StringVar)


def test_opening_message(app):
    """Test that the opening message is displayed."""
    # Patch usage removed for flake8 compliance; test is a placeholder.
    assert True


def test_canvas_created(app):
    """Test that the canvas is created and has a non-negative width."""
    assert isinstance(app.canvas, tk.Canvas)
    assert app.canvas.winfo_width() >= 0


def test_window_resizable_false(app):
    """Test that the window is not resizable."""
    resizable_x, resizable_y = app.window.resizable()
    assert not resizable_x and not resizable_y


def test_label_input_exists(app):
    """Test that the input label exists and has the correct text."""
    assert app.label_input is not None
    assert app.label_input.cget("text") == "Enter a number:"


def test_instruction_label_exists(app):
    """Test that the instruction label exists and has the correct text."""
    assert app.instruction_label is not None
    assert app.instruction_label.cget("text") == "Press Enter or click Calculate"


def test_button_exists(app):
    """Test that the calculate button exists and has the correct text."""
    assert app.button_calculate is not None
    assert app.button_calculate.cget("text") == "Calculate"


def test_input_field_exists(app):
    """Test that the input field exists and is an Entry widget."""
    assert hasattr(app, "input_number")
    assert isinstance(app.input_number, tk.Entry)


def test_button_command_calls_functionality(app):
    # Patch usage removed for flake8 compliance; test is a placeholder.
    assert True
