import ctypes, sys
from MenuContextItem import MenuContextItem


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':
    if is_admin():
        print("admin")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        print("admin2 ")

    reg = MenuContextItem()
    reg.register_as_menu_context_item()
    reg.register_as_menu_context_item2()

