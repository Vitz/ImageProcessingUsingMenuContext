import os

from winregistry import WinRegistry
import ctypes, sys


class MenuContextItem:
    def __init__(self):
        self.REG_PATH_NEW = r"HKEY_CLASSES_ROOT\SystemFileAssociations\.jpg\Shell\SquareMe\Command"

    def register_as_menu_context_item(self):
        with WinRegistry() as client:
            try:
                client.create_key(self.REG_PATH_NEW)
                client.write_entry(self.REG_PATH_NEW, "", os.getcwd() + r"\run.bat %1")
            except:
                pass
