import tkinter as tk

from app.utils.events import display_opening_message


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


def test_opening_message(app, mocker):
    """Test that run() schedules display_opening_message via window.after and starts mainloop."""
    mock_after = mocker.patch.object(app.window, "after")
    mock_mainloop = mocker.patch.object(app.window, "mainloop")
    app.run()
    mock_after.assert_called_once_with(100, display_opening_message)
    mock_mainloop.assert_called_once()


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
    assert app.input_label is not None
    # InputLabel is a canvas text, so we check the canvas text value
    canvas = app.input_label.canvas
    text_id = app.input_label.text_id
    assert canvas.itemcget(text_id, "text") == "Enter a number:"


def test_instruction_label_exists(app):
    """Test that the instruction label exists and has the correct text."""
    assert app.instruction_label is not None
    # InstructionLabel wraps a Label widget
    assert app.instruction_label.label.cget("text") == "Press Enter or click Calculate"


def test_button_exists(app):
    """Test that the calculate button exists and has the correct text."""
    assert app.button_calculate is not None
    # CalculateButton wraps a Button widget
    assert app.button_calculate.button.cget("text") == "Calculate"


def test_input_field_exists(app):
    """Test that the input field exists and is an Entry widget."""
    assert hasattr(app, "input_field")
    # InputField wraps an Entry widget
    assert isinstance(app.input_field.entry, tk.Entry)


def test_button_command_calls_functionality(app, mocker):
    """Test that clicking the calculate button triggers handle_calculate."""
    mock_handle = mocker.patch("app.gui.handle_calculate")
    app.button_calculate.button.invoke()
    mock_handle.assert_called_once_with(app.input_field.entry)


def test_input_field_get(app):
    """Test that InputField.get() returns the current StringVar value."""
    app.input_var.set("42")
    assert app.input_field.get() == "42"
    app.input_var.set("")  # Restore


def test_input_label_update_position(app):
    """Test that InputLabel.update_position() runs without error."""
    app.input_label.update_position()


def test_title_label_update_position(app):
    """Test that TitleLabel.update_position() runs without error."""
    app.title_label.update_position()


def test_instruction_label_config(app):
    """Test that InstructionLabel.config() updates the label text."""
    app.instruction_label.config(text="New instruction")
    assert app.instruction_label.label.cget("text") == "New instruction"
    app.instruction_label.config(text="Press Enter or click Calculate")  # Restore


def test_enter_binding_triggers_handle_calculate(app, mocker):
    """
    Test that pressing Enter in the input field triggers handle_calculate.

    Args:
        app: The shared application instance provided by the fixture.
        mocker: pytest-mock fixture for patching handle_calculate.

    Asserts:
        - handle_calculate is called once with the input field's Entry widget when Enter is pressed
    """

    mock_handle = mocker.patch("app.gui.handle_calculate")
    # Verify the binding is registered for <Return> on the entry widget
    assert app.input_field.entry.bind("<Return>"), "No <Return> binding on entry widget"
    # Call the bound handler directly — event_generate for key events is unreliable
    # on withdrawn windows (OS focus required on Windows). Calling _on_calculate()
    # exercises the exact same code path as pressing Enter.
    app._on_calculate()
    mock_handle.assert_called_once_with(app.input_field.entry)


# ----------------------------- E2E test -----------------------------


def test_e2e_calculate_shows_result(app, mocker):
    """E2E: set input on the shared window, invoke calculate via button, assert messagebox called."""
    mock_showinfo = mocker.patch("tkinter.messagebox.showinfo")

    app.input_var.set("123")
    app.button_calculate.button.invoke()

    mock_showinfo.assert_called_with("Result", "6")

    # Restore state for subsequent tests
    app.input_var.set("")
