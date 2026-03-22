import pytest
import tkinter as tk

from app.utils.tkinter_env import fix_tkinter_library_paths
from app.gui import Window

# Fix Tcl/Tk library paths for virtual environments on Windows.
fix_tkinter_library_paths()

# Patch iconbitmap to avoid failures on Linux/CI where .ico files are unsupported.
tk.Tk.iconbitmap = lambda *args, **kwargs: None


@pytest.fixture(scope="session")
def app():
    """Session-scoped Tkinter Window, shared across all test modules.

    Using a single Tk instance per test session avoids the Tcl/Tk interpreter
    state corruption that occurs when a Tk window is destroyed and a new one
    is created in the same process.
    """
    window = Window()
    window.__main__()
    window.window.withdraw()
    yield window
    window.window.destroy()
