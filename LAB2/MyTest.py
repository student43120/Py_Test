import os
import platform
import socket
import subprocess
import psutil
import sys
import argparse

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyTest")
        self.setFixedSize(800, 400)

        self.text_view = QLabel(self)
        self.text_view.setAlignment(Qt.AlignCenter)
        self.text_view.setFont(QFont("Arial", 14))
        self.text_view.setText("Welcome to MyTest!")

        ipv4_button = QPushButton("Moje Ipv4")
        ipv4_button.clicked.connect(self.get_ipv4)

        proxy_button = QPushButton("Czy jest uruchomione Proxy?")
        proxy_button.clicked.connect(self.check_proxy)

        os_button = QPushButton("Wersja systemu operacyjnego")
        os_button.clicked.connect(self.get_os_version)

        bios_button = QPushButton("Wersja BIOS")
        bios_button.clicked.connect(self.get_bios_version)

        hostname_button = QPushButton("Host name")
        hostname_button.clicked.connect(self.get_hostname)

        # help_button = QPushButton("Help")
        # help_button.clicked.connect(self.get_help)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)

        layout = QVBoxLayout()
        layout.addWidget(self.text_view)
        layout.addWidget(ipv4_button)
        layout.addWidget(proxy_button)
        layout.addWidget(os_button)
        layout.addWidget(bios_button)
        layout.addWidget(hostname_button)
        # layout.addWidget(help_button)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def get_ipv4(self):
        self.text_view.setText(get_ipv4())

    def check_proxy(self):
        self.text_view.setText(check_proxy())

    def get_os_version(self):
        self.text_view.setText(get_os_version())

    def get_bios_version(self):
        self.text_view.setText(get_bios_version())

    def get_hostname(self):
        self.text_view.setText(get_hostname())

    # def get_help(self):
    #     self.text_view.setText(get_help())

    def exit(self):
       self.close()

def get_ipv4():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    output = subprocess.check_output(["netsh", "winhttp", "show", "proxy"])
    output_str = output.decode("utf-8")
    if "Direct access (no proxy server)" in output_str:
        ip_type = "dynamicznie"
    else:
        ip_type = "statycznie"

    if os.name == 'nt':
        output = subprocess.check_output(["netsh", "interface", "show", "interface"])
        output_str = output.decode("utf-8")
        if "Wi-Fi" in output_str:
            connection_type = "Wi-Fi"
        else:
            connection_type = "Ethernet"
    else:
        output = subprocess.check_output(["nmcli", "-t", "-f", "TYPE,DEVICE", "device"])
        output_str = output.decode("utf-8")
        if "wifi" in output_str:
            connection_type = "Wi-Fi"
        else:
            connection_type = "Ethernet"
    message = f"Twój adres IPv4: {ip_address}.\nPrzydzielenie adresu IPv4: {ip_type}\nTyp połączenia: {connection_type}"
    return message

def check_proxy():
    if os.name == 'nt':
        output = subprocess.check_output(["netsh", "winhttp", "show", "proxy"])
        output_str = output.decode("utf-8")
        if "Direct access (no proxy server)" in output_str:
            message = "Nie jest uruchomione żadne proxy."
        else:
            message = "Uruchomione jest proxy."
            index = output_str.find(":") + 1
            ip_port_str = output_str[index:].strip()
            message += f"\nIP i port: {ip_port_str}"
    else:
        output = subprocess.check_output(["env", "|", "grep", "-i", "proxy"])
        output_str = output.decode("utf-8")
        if not output_str:
            message = "Nie jest uruchomione żadne proxy."
        else:
            message = "Uruchomione jest proxy.\n" + output_str
    return message

def get_os_version():
    os_version = platform.platform()
    cpu_count = os.cpu_count()

    if os.name == 'nt':
        total_memory = round(psutil.virtual_memory().total / (1024.0 **3))
    elif os.name == 'posix':
        total_memory = round((os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))/(1024.**3))
    message = f"Wersja systemu operacyjnego: {os_version}\nLiczba rdzeni: {cpu_count}\nPamięć RAM: {total_memory} GB"
    return message

def get_bios_version():
    bios_info = subprocess.check_output(["wmic", "bios", "get", "smbiosbiosversion"])
    bios_version = bios_info.decode("utf-8").split("\n")[1].strip()
    message = f"Wersja BIOS: {bios_version}"
    return message

def get_hostname():
    hostname = socket.gethostname()
    message = f"Host name: {hostname}"
    return message

def get_help():
    message = "\n".join([
        "".center(100,'#'),
        "#" + " MY TEST ".center(98,' ') + "#",
        "#" + "_ O PROGRAMIE ".ljust(98,'_') + "#",
        "#" + " Program służy do sprawdzenia parametrow sieciowych uzytkownika.".ljust(98,' ') + "#",
        "#" + " Moze byc obslugiwany zarowno okienkowo jak i z wiersza polecen.".ljust(98,' ') + "#",
        "#" + "".ljust(98,' ') + "#",
        "#" + "_ INSTRUKCJA DLA UZYTKOWNIKA ".ljust(98,'_') + "#",
        "#" + " Dostepne instrukcje w wierszu polecen: ".ljust(98,' ') + "#",
        "#" + "".ljust(98,' ') + "#",
        "#" + "_PARAMETR [SYSTEM]: ".ljust(98,'_') + "#",
        "#" + " - dla Windows: my_test.exe ".ljust(98,' ') + "#",
        "#" + " - dla Linux: my_test.ext4 ".ljust(98,' ') + "#",
        "#" + "".ljust(98,' ') + "#",
        "#" + "_KOMENDA ".ljust(98,'_') + "#",
        "#" + " - ipv4 - komenda: [SYSTEM] ipv4 ".ljust(98,' ') + "#",
        "#" + " - proxy - komenda: [SYSTEM] proxy ".ljust(98,' ') + "#",
        "#" + " - os - komenda: [SYSTEM] os ".ljust(98,' ') + "#",
        "#" + " - bios - komenda: [SYSTEM] bios ".ljust(98,' ') + "#",
        "#" + " - hostname - komenda: [SYSTEM] hostname ".ljust(98,' ') + "#",
        "#" + " - help - komenda: [SYSTEM] help ".ljust(98,' ') + "#",
        "#" + " Po wpisaniu komendy zatwierdzamy ją wciskajac enter. ".ljust(98,' ') + "#",
        "#" + "".ljust(98,' ') + "#",
        "#" + "_ WARNING ".ljust(98,'_') + "#",
        "#" + " Program dziala tylko dla systemów Windows lub Linux.".ljust(98,' ') + "#",
        "#" + "".ljust(98,'_') + "#",
        "".center(100,'#')
    ])
    return message

def handle_command_line(args):
    command_dict = {
      "ipv4": get_ipv4,
      "proxy": check_proxy,
      "os": get_os_version,
      "bios": get_bios_version,
      "hostname": get_hostname,
      "help": get_help
    }

    command_from_user = args[1]
    if command_from_user in command_dict:
        return command_dict[command_from_user]()
        

if __name__ == "__main__":
    if len(sys.argv) == 1: 
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()
    else:
        print(handle_command_line(sys.argv))