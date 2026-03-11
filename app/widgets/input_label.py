class InputLabel:
    """
    InputLabel widget for the Cross Sum Number App.

    This widget displays a label prompting the user to enter a number. It is designed to be centered on the canvas and can update its position dynamically when the window is resized.

    Attributes:
        canvas: The Canvas widget where the label is drawn.
        text_id: The ID of the text item on the canvas, used for updating its position.
    """

    def __init__(
        self, canvas, text="Enter a number:", font=("Arial", 14), fill="black", y=160
    ):
        """
        Initialize the input label widget.

        Args:
            canvas: The Canvas widget to draw the label on.
            text (str, optional): The label text. Defaults to "Enter a number:".
            font (tuple, optional): Font for the label. Defaults to ("Arial", 14).
            fill (str, optional): Text color. Defaults to "black".
            y (int, optional): Y-coordinate for the label. Defaults to 160.
        """
        self.canvas = canvas
        self.text_id = canvas.create_text(
            canvas.winfo_reqwidth() // 2 if canvas.winfo_reqwidth() else 300,
            y,
            text=text,
            font=font,
            fill=fill,
        )

    def update_position(self, y=None):
        """
        Update the position of the input label to keep it centered.

        Args:
            y (int, optional): New Y-coordinate. If None, keeps current.
        """
        width = self.canvas.winfo_width() or 600
        y_pos = y if y is not None else self.canvas.coords(self.text_id)[1]
        self.canvas.coords(self.text_id, width // 2, y_pos)
