class TitleLabel:
    """
    TitleLabel widget for the Cross Sum Number App.
    This widget displays the main title of the application. It is designed to be centered on the canvas and can update its position dynamically when the window is resized.
    Attributes:
        canvas: The Canvas widget where the title is drawn.
        text_id: The ID of the text item on the canvas, used for updating its position.
    """

    def __init__(
        self, canvas, text="Cross Sum Number", font=("Arial", 24, "bold"), fill="black"
    ):
        """
        Initialize the title label widget.

        Args:
            canvas: The Canvas widget to draw the title on.
            text (str, optional): The title text. Defaults to "Cross Sum Number".
            font (tuple, optional): Font for the title. Defaults to ("Arial", 24, "bold").
            fill (str, optional): Text color. Defaults to "black".
        """
        self.canvas = canvas
        self.text_id = canvas.create_text(
            canvas.winfo_reqwidth() // 2 if canvas.winfo_reqwidth() else 300,
            40,
            text=text,
            font=font,
            fill=fill,
        )

    def update_position(self):
        """
        Update the position of the title label to keep it centered.
        """
        width = self.canvas.winfo_width() or 600
        self.canvas.coords(self.text_id, width // 2, 40)
