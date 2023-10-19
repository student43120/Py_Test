import os
import platform
import socket
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("MyTest")
        self.setFixedSize(400, 300)

     
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

       
        layout = QVBoxLayout()
        layout.addWidget(self.text_view)
        layout.addWidget(ipv4_button)
        layout.addWidget(proxy_button)
        layout.addWidget(os_button)
        layout.addWidget(bios_button)
        layout.addWidget(hostname_button)

        
        self.setLayout(layout)

    def get_ipv4(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        if ip_address.startswith("127."):
            message = "Nie udało się uzyskać adresu IP."
            self.text_view.setText(message)
            return

        message = f"Twój adres IPv4 to {ip_address}."
        self.text_view.setText(message)

    def check_proxy(self):
        try:
            output = subprocess.check_output(["netsh", "winhttp", "show", "proxy"])
            output_str = output.decode("utf-8")
            if "Direct access (no proxy server)" in output_str:
                message = "Nie jest uruchomione żadne proxy."
            else:
                message = "Uruchomione jest proxy."
                index = output_str.find(":") + 1
                ip_port_str = output_str[index:].strip()
                message += f"\nIP i port: {ip_port_str}"
            self.text_view.setText(message)

        except subprocess.CalledProcessError:
            message = "Nie udało się sprawdzić ustawień proxy."
            self.text_view.setText(message)

    def get_os_version(self):
        os_version = platform.platform()
        cpu_count = os.cpu_count()
        total_memory = round((os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))/(1024.**3))
        message = f"Wersja systemu operacyjnego: {os_version}\nLiczba rdzeni: {cpu_count}\nPamięć RAM: {total_memory} GB"
        self.text_view.setText(message)

    def get_bios_version(self):
        try:
            bios_info = subprocess.check_output(["wmic", "bios", "get", "smbiosbiosversion"])
            bios_version = bios_info.decode("utf-8").split("\n")[1].strip()
            message = f"Wersja BIOS: {bios_version}"
        except Exception as e:
            message = f"Wystąpił błąd podczas pobierania wersji BIOS: {e}"

        self.text_view.setText(message)

    def get_hostname(self):
        hostname = socket.gethostname()
        message = f"Host name: {hostname}"
        self.text_view.setText(message)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()