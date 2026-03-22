from tkinter import Tk
from typing import Optional, Tuple
from app.utils.icon import get_icon_path


class WindowSetup:
    """
    Utility class for setting up the main application window.

    This class handles the configuration of the Tkinter window, including title, geometry, resizability, and icon setup. It ensures that the application window is initialized with consistent properties across different platforms.

    Attributes:
        root: The Tk root window.
        title: The window title.
        width: The window width.
        height: The window height.
        resizable: A tuple indicating whether the window is resizable in width and height.
        icon_path: The path to the window icon.
        center: Whether to center the window on the screen.

    """

    def __init__(
        self,
        root: Tk,
        title: str = "Cross Sum Calculator",
        width: int = 600,
        height: int = 400,
        resizable: Tuple[bool, bool] = (False, False),
        icon_path: Optional[str] = None,
        center: bool = True,
    ):
        """
        Initialize and configure the main application window.

        Args:
            root: The Tk root window.
            title (str, optional): The window title. Defaults to "Cross Sum Calculator".
            width (int, optional): Window width. Defaults to 600.
            height (int, optional): Window height. Defaults to 400.
            resizable (tuple, optional): (width, height) resizability. Defaults to (False, False).
            icon_path (str, optional): Path to the window icon. If None, uses default from get_icon_path().
            center (bool, optional): Whether to center the window on the screen. Defaults to True.
        """
        self.root = root
        self.title = title
        self.width = width
        self.height = height
        self.resizable = resizable
        self.icon_path = (
            icon_path
            if icon_path is not None
            else get_icon_path("app/assets/icon/Icon.ico")
        )

        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(*self.resizable)
        if self.icon_path:
            try:
                self.root.iconbitmap(self.icon_path)
            except Exception:
                pass  # Ignore icon errors for cross-platform compatibility
        if center:
            self.center_window()

    def center_window(self):
        """
        Center the window on the screen.
        """
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
