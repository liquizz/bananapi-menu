import psutil
import subprocess
import sys
from subprocess import check_output
from bananapi_menu.settings import BASE_DIR


def function():
    if psutil.pid_exists(9382):
        return 1
    else:
        return 0

def LaunchNetCapture():
    #subprocess.call(["systemctl", "start", "NetCapture"])
    try:
        check = "NetCapture is currently running at: " + str(int(check_output(["pidof", "main.out"]))) + " pid"
    except subprocess.CalledProcessError:
        subprocess.call(["systemctl", "start", "NetCapture"])#"The process cannot be opened"
        check = "NetCapture started."
    return check

def StopNetCapture():
    try:
        check_output(["pidof", "main.out"])
        subprocess.call(["systemctl", "stop", "NetCapture"])
        msg = "The NetCapture was stopped."
    except subprocess.CalledProcessError:
        msg = "NetCapture is not running now."
    return msg

def PPPoEConfig():
    pid = subprocess.call(["pppoe"])
    if(pid == 0):
        return "OK"
    #return pid

