import psutil
import subprocess
import sys
from bananapi_menu.settings import BASE_DIR


def function():
    if psutil.pid_exists(9382):
        return 1
    else:
        return 0

def LaunchProcess():
    Content = subprocess.call([BASE_DIR + "/menu/scripts/main.out"], )
    return Content