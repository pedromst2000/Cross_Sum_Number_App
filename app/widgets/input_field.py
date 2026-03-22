from tkinter import Entry


class InputField:
    """
    Widget for user input, encapsulating a Tkinter Entry.

    Attributes:
        entry (Entry): The Tkinter Entry widget instance.
    """

    def __init__(
        self,
        parent,
        textvariable,
        font=("Arial", 14),
        width=20,
        borderwidth=6,
        relief="sunken",
    ):
        """
        Initialize the input field widget.

        Args:
            parent: Parent widget (usually a Canvas or Frame).
            textvariable: Tkinter StringVar for input binding.
            font (tuple, optional): Font for the input field. Defaults to ("Arial", 14).
            width (int, optional): Width of the input field. Defaults to 20.
            borderwidth (int, optional): Border width of the input field. Defaults to 6.
            relief (str, optional): Relief style of the input field. Defaults to "sunken".
        """
        self.entry: Entry = Entry(
            parent,
            textvariable=textvariable,
            font=font,
            width=width,
            borderwidth=borderwidth,
            relief=relief,
        )

    def place(self, x: int, y: int) -> None:
        """
        Place the input field at the given coordinates.

        Args:
            x (int): X-coordinate for placement.
            y (int): Y-coordinate for placement.
        """
        self.entry.update_idletasks()
        self.entry.place(x=x, y=y)

    def focus_set(self) -> None:
        """
        Set focus to the input field.
        """
        return self.entry.focus_set()

    def bind(self, sequence: str, func) -> None:
        """
        Bind an event to the input field.

        Args:
            sequence (str): The event sequence (e.g., '<Return>').
            func (callable): The callback function to bind.
        """
        return self.entry.bind(sequence, func)

    def get(self) -> str:
        """
        Get the current value from the input field.

        Returns:
            str: The current value in the input field.
        """
        return self.entry.get()
