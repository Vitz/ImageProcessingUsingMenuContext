import os
from winregistry import WinRegistry
import ctypes, sys

class MenuContextItem:
    def __init__(self):
        pass

    def register_as_menu_context_item(self):
        self.REG_PATH_NEW = r"HKEY_CLASSES_ROOT\SystemFileAssociations\.jpg\Shell\QuickSquareMe\Command"
        with WinRegistry() as client:
            try:
                client.create_key(self.REG_PATH_NEW)
                client.write_entry(self.REG_PATH_NEW, "", os.getcwd() + r"\run.bat %1")
            except:
                pass

    def register_as_menu_context_item2(self):
        self.REG_PATH_NEW = r"HKEY_CLASSES_ROOT\SystemFileAssociations\.jpg\Shell\QuickReduceMe10\Command"
        with WinRegistry() as client:
            try:
                client.create_key(self.REG_PATH_NEW)
                client.write_entry(self.REG_PATH_NEW, "", os.getcwd() + r"\run2.bat %1")
            except:
                pass

    def register_as_menu_context_item_png(self):
        self.REG_PATH_NEW = r"HKEY_CLASSES_ROOT\SystemFileAssociations\.png\Shell\QuickSquareMe\Command"
        with WinRegistry() as client:
            try:
                client.create_key(self.REG_PATH_NEW)
                client.write_entry(self.REG_PATH_NEW, "", os.getcwd() + r"\run.bat %1")
            except:
                pass

    def register_as_menu_context_item2_png(self):
        self.REG_PATH_NEW = r"HKEY_CLASSES_ROOT\SystemFileAssociations\.png\Shell\QuickReduceMe10\Command"
        with WinRegistry() as client:
            try:
                client.create_key(self.REG_PATH_NEW)
                client.write_entry(self.REG_PATH_NEW, "", os.getcwd() + r"\run2.bat %1")
            except:
                pass
