import os
import sys


def fix_tkinter_library_paths():
    """
    Fix Tcl/Tk library paths for virtual environments on Windows.

    This function sets the TCL_LIBRARY and TK_LIBRARY environment variables to the correct
    paths for Tcl/Tk when running inside a virtual environment on Windows.

    """
    if sys.platform == "win32" and sys.prefix != sys.base_prefix:
        _tcl_dir = os.path.join(sys.base_prefix, "tcl")
        if os.path.exists(_tcl_dir):
            for _item in os.listdir(_tcl_dir):
                _full = os.path.join(_tcl_dir, _item)
                if os.path.isdir(_full):
                    if _item.startswith("tcl") and os.path.exists(
                        os.path.join(_full, "init.tcl")
                    ):
                        os.environ["TCL_LIBRARY"] = _full
                    elif _item.startswith("tk") and os.path.exists(
                        os.path.join(_full, "tk.tcl")
                    ):
                        os.environ["TK_LIBRARY"] = _full
