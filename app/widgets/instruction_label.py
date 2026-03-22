from tkinter import Label


class InstructionLabel:
    """
    Widget for displaying instructions, encapsulating a Tkinter Label.

    Attributes:
        label (Label): The Tkinter Label widget instance.
    """

    def __init__(
        self,
        parent,
        text="Press Enter or click Calculate",
        font=("Arial", 12),
        fg="gray",
    ):
        """
        Initialize the instruction label widget.

        Args:
            parent: Parent widget (usually a Canvas or Frame).
            text (str, optional): Label text. Defaults to "Press Enter or click Calculate".
            font (tuple, optional): Font for the label. Defaults to ("Arial", 12).
            fg (str, optional): Foreground (text) color. Defaults to "gray".
        """
        self.label: Label = Label(
            parent,
            text=text,
            font=font,
            fg=fg,
        )

    def place(self, x: int, y: int) -> None:
        """
        Place the label at the given coordinates.

        Args:
            x (int): X-coordinate for placement.
            y (int): Y-coordinate for placement.

        """
        self.label.update_idletasks()
        self.label.place(x=x, y=y)

    def config(self, **kwargs) -> None:
        """
        Configure label options.

        Args:
            **kwargs: Keyword arguments for label configuration (e.g., text, font, fg).
        """
        self.label.config(**kwargs)
