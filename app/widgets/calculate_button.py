from tkinter import Button


class CalculateButton:
    """
    Widget for triggering calculations, encapsulating a Tkinter Button.

    Attributes:
        button (Button): The Tkinter Button widget instance.
    """

    def __init__(
        self,
        parent,
        text="Calculate",
        font=("Arial", 14),
        bg="lightblue",
        fg="black",
        command=None,
    ):
        """
        Initialize the calculate button widget.

        Args:
            parent: Parent widget (usually a Canvas or Frame).
            text (str, optional): Button text. Defaults to "Calculate".
            font (tuple, optional): Font for the button. Defaults to ("Arial", 14).
            bg (str, optional): Background color. Defaults to "lightblue".
            fg (str, optional): Foreground (text) color. Defaults to "black".
            command (callable, optional): Function to call on click. Defaults to None.
        """
        self.button: Button = Button(
            parent,
            text=text,
            font=font,
            bg=bg,
            fg=fg,
            command=command,
        )

    def place(self, x: int, y: int) -> None:
        """
        Place the button at the given coordinates.

        Args:
            x (int): X-coordinate for placement.
            y (int): Y-coordinate for placement.

        Returns:
            None
        """
        self.button.update_idletasks()
        self.button.place(x=x, y=y)
