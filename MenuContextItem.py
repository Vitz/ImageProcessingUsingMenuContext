import os
from winregistry import WinRegistry


class MenuContextItem:
    def __init__(self, name: str):
        self.name_safe = name

    def to_verbose(self, ):
        return self.name_safe.replace("-", " ").replace("_", " ").replace("P", "%").capitalize()


class MenuContextCreator:
    def __init__(self, items):
        self.extensions = ["png", "jpg", "jpeg", "webp"]
        self.items = items

    @staticmethod
    def __create_path(ext, name):
        return fr"HKEY_CLASSES_ROOT\SystemFileAssociations\.{ext}\Shell\{name}\Command"

    @staticmethod
    def __create_dir_path(name):
        return fr"HKEY_CLASSES_ROOT\Directory\shell\{name}\command"

    def register_functions_as_menu_context_item(self):
        for item in self.items:
            if not str(item.name_safe).endswith("_dir"):
                for ext in self.extensions:
                    reg_path = MenuContextCreator.__create_path(ext, item.to_verbose())
                    with WinRegistry() as client:
                        try:
                            client.create_key(reg_path)
                            client.write_entry(reg_path, "", os.getcwd() + fr"\ImageRunners\{item.name_safe}.bat %1")
                        except:
                            pass

    def register_functions_as_dir_menu_context_item(self):
        for item in self.items:
            if str(item.name_safe).endswith("_dir"):
                    reg_path = MenuContextCreator.__create_dir_path(item.to_verbose())
                    with WinRegistry() as client:
                        try:
                            client.create_key(reg_path)
                            client.write_entry(reg_path, "", os.getcwd() + fr"\ImageRunners\{item.name_safe}.bat %1")
                        except Exception as e:
                            pass


    def get_menu_items(self):
        return self.items
