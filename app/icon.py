import os
import sys


def get_icon_path(relative_path: str) -> str:
    """
    Get the absolute path to the application icon, compatible with both development
    and PyInstaller executable environments.

    :param relative_path: Relative path to the icon file.
    :return: Absolute path to the icon file.
    """

    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))

    return os.path.join(base_path, relative_path)
