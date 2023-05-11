import ctypes, sys

from ImageEditor import ImageEditor
from MenuContextItem import MenuContextItem, MenuContextCreator
from RunnersCreator import RunnersCreator


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def get_functions_names():
    import inspect
    out = []
    module = inspect.getmembers(ImageEditor)
    for m in module:
        if str(m[0]).startswith("quick"):
            out.append(str(m[0]))
    return out


if __name__ == '__main__':
    if is_admin():
        print("Admin privilege")
    else:
        print("Ask for Admin privilege")
        ctypes.windll.shell32.ShellExecuteW(None,
                                            "runas",
                                            sys.executable,
                                            " ".join(sys.argv),
                                            None,
                                            1)

    scripts = [MenuContextItem(x) for x in get_functions_names()]
    mm = MenuContextCreator(scripts)
    mm.clean()
    mm.register_functions_as_menu_context_item()
    _ = RunnersCreator(mm.get_menu_items())

