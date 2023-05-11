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


    def clean(self):
        for ext in self.extensions:
            path = fr"HKEY_CLASSES_ROOT\SystemFileAssociations\.{ext}\Shell"

            with WinRegistry() as client:
                try:
                    client.delete_key(path)
                except Exception as e:
                    print( e)

    @staticmethod
    def __create_path(ext, name):
        return fr"HKEY_CLASSES_ROOT\SystemFileAssociations\.{ext}\Shell\{name}\Command"

    def register_functions_as_menu_context_item(self):
        for item in self.items:
            for ext in self.extensions:
                reg_path = MenuContextCreator.__create_path(ext, item.to_verbose())
                with WinRegistry() as client:
                    try:
                        client.create_key(reg_path)
                        client.write_entry(reg_path, "", os.getcwd() + fr"\ImageRunners\{item.name_safe}.bat %1")
                    except:
                        pass

    def get_menu_items(self):
        return self.items
