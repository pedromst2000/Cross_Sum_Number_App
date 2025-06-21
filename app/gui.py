from tkinter import Tk, Label, Button, StringVar, Entry, messagebox, Canvas, ttk
from app.cross_sum import show_message
from app.icon import get_icon_path


class Window:
    AppIcon : str = None
    window: Tk = None
    canvas: Canvas = None
    label_input: Label = None
    button_calculate: Button = None
    input_var: StringVar = None
    result_var: StringVar = None

    def __init__(
        self,
        AppIcon: str = None,
        window: Tk = None,
        canvas: ttk.Frame = None,
        label_input: Label = None,
        button_calculate: Button = None,
        input_var: StringVar = None,
        result_var: StringVar = None,
    ):
        """
        Initialize the main class with optional parameters for window, canvas, input_var, and result_var.
        If no parameters are provided, it initializes the main window and canvas.

        :param AppIcon: Path to the application icon.
        :param window: Tk instance for the main window.
        :param canvas: ttk.Frame instance for the main canvas.
        :param label_input: Label instance for the input label.
        :param button_calculate: Button instance for the calculate button.
        :param input_var: StringVar instance for the input variable.
        :param result_var: StringVar instance for the result variable.
        """

        self.AppIcon = AppIcon if AppIcon is not None else "assets/icon/icon.ico"
        self.window = window
        self.canvas = canvas
        self.label_input = label_input
        self.button_calculate = button_calculate
        self.input_var = input_var
        self.result_var = result_var

    def __main__(self):
        """
        This method initializes the main window and canvas if they are not already set.
        """

        self.window = Tk()
        self.window.iconbitmap(get_icon_path(self.AppIcon))  # Set the application icon.
        self.window.title("Cross Sum Number")
        width, height = 600, 400
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)
        self.window.update_idletasks()  # Update the window to get the correct dimensions.
        screen_width = self.window.winfo_screenwidth()  # Get the width of the screen.
        screen_height = (
            self.window.winfo_screenheight()
        )  # Get the height of the screen.
        x = (screen_width // 2) - (
            width // 2
        )  # Calculate the x position to center the window.
        y = (screen_height // 2) - (
            height // 2
        )  # Calculate the y position to center the window.
        self.window.geometry(
            f"{width}x{height}+{x}+{y}"
        )  # Setting the geometry of the window to center it on the screen.

        self.input_var = StringVar()  # StringVar to hold the input value.
        self.result_var = StringVar()  # StringVar to hold the result value.
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)

        # Title
        self.canvas.create_text(
            width // 2,
            40,
            text="Cross Sum Number",
            font=("Arial", 24, "bold"),
            fill="black",
        )

        # Layout configuration
        y_start = 90
        y_spacing = 60

        # Instruction label
        self.instruction_label = Label(
            self.canvas,
            text="Press Enter or click Calculate",
            font=("Arial", 12),
            fg="gray",
        )
        self.instruction_label.update_idletasks()
        self.instruction_label.place(
            x=(width // 2) - (self.instruction_label.winfo_reqwidth() // 2),
            y=y_start,
        )

        # Input label
        self.label_input = Label(
            self.canvas,
            text="Enter a number:",
            font=("Arial", 14),
        )
        self.label_input.update_idletasks()
        self.label_input.place(
            x=(width // 2) - (self.label_input.winfo_reqwidth() // 2),
            y=y_start + y_spacing,
        )

        # Input field
        self.input_number = Entry(
            self.canvas,
            textvariable=self.input_var,
            font=("Arial", 14),
            width=20,
            borderwidth=6,
            relief="sunken",
        )
        self.input_number.update_idletasks()
        self.input_number.place(
            x=(width // 2) - (self.input_number.winfo_reqwidth() // 2),
            y=y_start + 2 * y_spacing,
        )

        # to focus on the input field when the window opens
        self.input_number.focus_set()

        # Calculate button
        self.button_calculate = Button(
            self.canvas,
            text="Calculate",
            font=("Arial", 14),
            bg="lightblue",
            fg="black",
        )
        self.button_calculate.update_idletasks()
        self.button_calculate.place(
            x=(width // 2) - (self.button_calculate.winfo_reqwidth() // 2),
            y=y_start + 3 * y_spacing,
        )

        self.button_calculate.config(command=self.handle_calculate)
        self.input_number.bind("<Return>", lambda event: self.handle_calculate())

    def handle_calculate(self):
        """
        Handle the calculate button click event.
        """
        show_message(messagebox, self.input_number.get())

    def display_opening_message(self):
        """
        Display an opening message in the Tkinter window.
        """
        messagebox.showinfo(
            "Welcome",
            "Welcome to the Cross Sum Number application!\n"
            "A cross sum is the sum of all digits in a number.\n"
            "For example, the cross sum of 12345 is 1 + 2 + 3 + 4 + 5 = 15.\n"
        )

    def run(self):
        """
        Run the main loop of the Tkinter window.
        """
        if self.window is None:
            self.__main__()
        # Show the opening message after the window is initialized
        self.window.after(100, self.display_opening_message)
        self.window.mainloop()
