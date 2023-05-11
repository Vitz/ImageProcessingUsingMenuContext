import os
from winregistry import WinRegistry
import ctypes, sys
from pathlib import Path


class Runner:
    def __init__(self, safe_name):
        self.safe_name = safe_name

    def __get_command(self):
        env = os.environ["VIRTUAL_ENV"] + r"\Scripts"
        exe_dir = os.getcwd()
        return fr'cmd /k "cd /d {env} & activate & cd /d {exe_dir} & python main.py --{self.safe_name} %* & Exit" '

    def create(self):
        # # home = str(Path.home()) + r"\ImageRunners"
        # try:
        #     os.mkdir(home)
        # except:
        #     pass

        with open(rf"ImageRunners/{self.safe_name}.bat", "w", encoding="utf-8") as f:
            f.write("@echo off \n")
            val = self.__get_command()
            f.write(val)
            f.close()


class RunnersCreator:
    def __init__(self, items):
        runners = [Runner(item.name_safe) for item in items]
        for runner in runners:
            runner.create()


