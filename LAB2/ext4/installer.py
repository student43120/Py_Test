import os
import platform
import socket
import subprocess

try:
    subprocess.check_call(["sudo", "apt-get", "update"])
    subprocess.check_call(["sudo", "apt-get", "install", "-f"])
    subprocess.check_call(["sudo", "apt-get", "install", "python3-pip"])
    #subprocess.check_call(["sudo", "pip3", "install", "os"])
    #subprocess.check_call(["sudo", "pip3", "install", "platform"])
    #subprocess.check_call(["sudo", "pip3", "install", "socket"])
    #subprocess.check_call(["sudo", "pip3", "install", "subprocess"])
    subprocess.check_call(["sudo", "pip3", "install", "psutil"])
    subprocess.check_call(["sudo", "pip3", "install", "PyQt5"])
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

if platform.system() == "Linux":
    with open(os.path.expanduser("~/.bashrc"), "a") as f:
        f.write("sudo python3 installer.py\n")
