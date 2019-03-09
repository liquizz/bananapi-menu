import psutil
import subprocess

def function():
    if psutil.pid_exists(4220):
        return 1
    else:
        return 0