import os
import sys


def fix_tkinter_library_paths():
    """
    Fix Tcl/Tk library paths for virtual environments on Windows.
    When running inside .venv, Python cannot find Tcl/Tk files from the base install.
    This finds the exact directory that contains init.tcl and sets TCL_LIBRARY to it.
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
