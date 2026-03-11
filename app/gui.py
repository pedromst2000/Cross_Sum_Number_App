from tkinter import Tk, StringVar, Canvas
from app.widgets.input_field import InputField
from app.widgets.calculate_button import CalculateButton
from app.widgets.instruction_label import InstructionLabel
from app.widgets.title_label import TitleLabel
from app.widgets.input_label import InputLabel
from app.utils.window_setup import WindowSetup
from app.utils.events import display_opening_message, handle_calculate


class Window:
    """
    Main application window for Cross Sum Number App.

    This class initializes the main Tkinter window, sets up the layout, and composes the widgets.
    """

    def __init__(
        self,
        AppIcon: str = None,
        window: Tk = None,
        canvas: Canvas = None,
        input_var: StringVar = None,
        result_var: StringVar = None,
        input_field: InputField = None,
        button_calculate: CalculateButton = None,
        instruction_label: InstructionLabel = None,
        title_label: TitleLabel = None,
        input_label: InputLabel = None,
    ):
        """
        Initialize the main Window class.

        Args:
            AppIcon (str, optional): Path to the application icon. Defaults to None.
            window (Tk, optional): Tkinter window instance. Defaults to None.
            canvas (Canvas, optional): Canvas widget. Defaults to None.
            input_var (StringVar, optional): Input StringVar. Defaults to None.
            result_var (StringVar, optional): Result StringVar. Defaults to None.
            input_field (InputField, optional): InputField widget. Defaults to None.
            button_calculate (CalculateButton, optional): CalculateButton widget. Defaults to None.
            instruction_label (InstructionLabel, optional): InstructionLabel widget. Defaults to None.
            title_label (TitleLabel, optional): TitleLabel widget. Defaults to None.
            input_label (InputLabel, optional): InputLabel widget. Defaults to None.
        """
        self.AppIcon: str = (
            AppIcon if AppIcon is not None else "app/assets/icon/Icon.ico"
        )
        self.window = window
        self.canvas = canvas
        self.input_var = input_var
        self.result_var = result_var
        self.input_field = input_field
        self.button_calculate = button_calculate
        self.instruction_label = instruction_label
        self.title_label = title_label
        self.input_label = input_label

    def __main__(self):
        """
        Set up the main window and compose widgets.

        This method initializes the Tkinter window, sets its properties, and adds all UI widgets.
        """
        # ---------------------------------Window setup ---------------------------
        self.window = Tk()
        window_setup = WindowSetup(
            self.window,
            title="Cross Sum Number",
            width=600,
            height=400,
            resizable=(False, False),
            center=True,
        )
        self.width = window_setup.width
        self.height = window_setup.height

        # ---------------------------------Widgets setup ---------------------------

        # Initialize StringVars for input and result
        self.input_var = StringVar()
        self.result_var = StringVar()
        self.canvas = Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack(fill="both", expand=True)

        # Title label widget
        self.title_label = TitleLabel(self.canvas)

        # Layout configuration
        y_start = 90
        y_spacing = 60

        # Instruction label widget
        self.instruction_label = InstructionLabel(self.canvas)
        self.instruction_label.place(
            x=(self.width // 2) - (self.instruction_label.label.winfo_reqwidth() // 2),
            y=y_start,
        )

        # Input label widget
        self.input_label = InputLabel(self.canvas, y=y_start + y_spacing + 10)

        # Input field widget
        self.input_field = InputField(self.canvas, textvariable=self.input_var)
        self.input_field.place(
            x=(self.width // 2) - (self.input_field.entry.winfo_reqwidth() // 2),
            y=y_start + 2 * y_spacing,
        )
        self.input_field.focus_set()

        # Calculate button widget
        self.button_calculate = CalculateButton(
            self.canvas, command=lambda: handle_calculate(self.input_field.entry)
        )
        self.button_calculate.place(
            x=(self.width // 2) - (self.button_calculate.button.winfo_reqwidth() // 2),
            y=y_start + 3 * y_spacing,
        )

        # Bind Enter key to calculation
        self.input_field.bind(
            "<Return>", lambda event: handle_calculate(self.input_field.entry)
        )

    def run(self):
        """
        Start the Tkinter main loop to display the window.

        If the window is not initialized, it will be set up first. Then, the opening message is shown and the main loop is started.
        """
        if self.window is None:
            self.__main__()
        # Show the opening message after the window is initialized
        self.window.after(100, display_opening_message)
        self.window.mainloop()
