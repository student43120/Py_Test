import os
import platform
import socket
import subprocess

try:
    subprocess.check_call(["sudo", "apt-get", "update"])
    subprocess.check_call(["sudo", "apt-get", "install", "-f"])
    subprocess.check_call(["sudo", "apt-get", "install", "python3-pip"])
    subprocess.check_call(["sudo", "pip3", "install", "psutil"])
    subprocess.check_call(["sudo", "pip3", "install", "PyQt5"])
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

class HelpWindow(QMainWindow):
    def __init__(self, message):
        super(HelpWindow, self).__init__()

        self.setWindowTitle("Pomoc dla MyTest")
        self.setFixedSize(1500, 800)

        self.text_view = QLabel(self)
        self.text_view.setAlignment(Qt.AlignCenter)
        self.text_view.setFont(QFont("Arial", 14))
        self.text_view.setText(message)
        self.setCentralWidget(self.text_view)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyTest")
        self.setFixedSize(1000, 400)

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

        help_button = QPushButton("Help")
        help_button.clicked.connect(self.get_help)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit)

        layout = QVBoxLayout()
        layout.addWidget(self.text_view)
        layout.addWidget(ipv4_button)
        layout.addWidget(proxy_button)
        layout.addWidget(os_button)
        layout.addWidget(bios_button)
        layout.addWidget(hostname_button)
        layout.addWidget(help_button)
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

    def get_help(self):
        message = "\n".join([
        "".center(80,'#'),
        "#" + " MY TEST ".center(199,' ') + "#",
        "__ O PROGRAMIE ".ljust(130,'_'),
        "".ljust(200,' '),
        " Program służy do sprawdzenia parametrow sieciowych uzytkownika.".ljust(200,' '),
        " Moze byc obslugiwany zarowno okienkowo jak i z wiersza polecen.".ljust(200,' '),
        "".ljust(200,' '),
        "__ INSTRUKCJA DLA UZYTKOWNIKA ".center(130,'_'),
        "".ljust(200,' '),
        "__DEDYKOWANY PLIK PER SYSTEM: ".ljust(130,'_'),
        "".ljust(200,' '),
        " - dla Windows: my_test.exe ".ljust(96,' '),
        " - dla Linux: my_test.ext4 ".ljust(96,' '),
        "".ljust(200,' '),
        "__FUNKCJONALNOŚCI ".ljust(130,'_'),
        "".ljust(200,' '),
        " -- SPRAWDZA ADRES IPV4 UZYTKOWNIKA: Przycisk --> Moje Ipv4".ljust(96,' '),
        " -- SPRAWDZA CZY UZYTKOWNIK KORZYSTA Z PROXY: Przycisk --> Czy jest uruchomione Proxy?".ljust(96,' '),
        " -- SPRAWDZA JAKI SYSTEM MA UZYTKOWNIK: Przycisk --> Wersja systemu operacyjnego".ljust(96,' '),
        " -- SPRAWDZA JAKI BIOS MA UZYTKOWNIK: Przycisk --> Wersja BIOS".ljust(96,' '),
        " -- SPRAWDZA JAKA NAZWE MA URZADZENIE UZYTKOWNIKA: Przycisk --> Host name".ljust(96,' '),
        " -- WYSWIETLA POMOC DLA UZYTKOWNIKA: Przycisk --> Help".ljust(96,' '),
        " -- ZAMYKA PROGRAM: Przycisk --> Exit".ljust(96,' '),
        "".ljust(200,' '),
        "__ WARNING ".ljust(130,'_'),
        "".ljust(200,' '),
        " Program dziala tylko dla systemów Windows lub Linux.".ljust(96,' '),
        " Dla systemów Linux prosimy o uruchomienie programu z sudo (w innym wypadku niektóre opcje moga byc niedostepne).".ljust(96,' '),
        "#" + "".ljust(130,'_') + "#",
        "".center(80,'#')
    ])
        self.help_window = HelpWindow(message)
        self.help_window.show()

    def exit(self):
       self.close()
       self.help_window.close()

def get_ipv4():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    if os.name == 'nt':
        output = subprocess.check_output(["netsh", "winhttp", "show", "proxy"])
        output_str = output.decode("utf-8")
        if "Direct access (no proxy server)" in output_str:
            ip_type = "dynamicznie"
        else:
            ip_type = "statycznie"

        output = subprocess.check_output(["netsh", "interface", "show", "interface"])
        output_str = output.decode("utf-8")
        if "Wi-Fi" in output_str:
            connection_type = "Wi-Fi"
        else:
            connection_type = "Ethernet"

    if os.name == 'posix':
        output = subprocess.check_output(["ip", "addr"])
        output_str = output.decode("utf-8")
        ip_info = [line for line in output_str.splitlines() if "127." not in line and "inet6" not in line and "inet" in line][0]
        ip_address = ip_info.strip().split(' ')[1].split('/')[0]
        ip_type = "dynamicznie" if "dynamic" in ip_info else "statycznie"

        output = subprocess.check_output(["nmcli", "-t", "connection", "show", "--active"])
        output_str = output.decode("utf-8")
        if "802-11-wireless" in output_str:
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
        p1 = subprocess.Popen(["env"], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-i", "proxy"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p2.communicate()[0]
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
    message = "Wersja BIOS nieodnaleziona"
    if os.name == 'nt':
        bios_info = subprocess.check_output(["wmic", "bios", "get", "smbiosbiosversion"])
        bios_version = bios_info.decode("utf-8").split("\n")[1].strip()
        message = f"Wersja BIOS: {bios_version}"

    if os.name == 'posix':
        bios_info = subprocess.check_output(["sudo", "dmidecode", "-t", "bios"])
        bios_info_str = bios_info.decode("utf-8")
        for line in bios_info_str.split("\n"):
            if "Version:" in line:
                bios_version = line.split(":")[1].strip()
                message = f"Wersja BIOS: {bios_version}"
    return message

def get_hostname():
    hostname = socket.gethostname()
    message = f"Host name: {hostname}"
    return message

def get_help():
    message = "\n".join([
        "".center(120,'#'),
        "#" + " MY TEST ".center(118,' ') + "#",
        "#" + "_ O PROGRAMIE ".ljust(118,'_') + "#",
        "#" + " Program służy do sprawdzenia parametrow sieciowych uzytkownika.".ljust(118,' ') + "#",
        "#" + " Moze byc obslugiwany zarowno okienkowo jak i z wiersza polecen.".ljust(118,' ') + "#",
        "#" + "".ljust(118,' ') + "#",
        "#" + "_ INSTRUKCJA DLA UZYTKOWNIKA ".ljust(118,'_') + "#",
        "#" + " Dostepne instrukcje w wierszu polecen: ".ljust(118,' ') + "#",
        "#" + "".ljust(118,' ') + "#",
        "#" + "_PARAMETR [SYSTEM]: ".ljust(118,'_') + "#",
        "#" + " - dla Windows: my_test.exe ".ljust(118,' ') + "#",
        "#" + " - dla Linux: my_test.ext4 ".ljust(118,' ') + "#",
        "#" + "".ljust(118,' ') + "#",
        "#" + "_FUNKCJONALNOŚCI ".ljust(118,'_') + "#",
        "#" + " - SPRAWDZA ADRES IPV4 UZYTKOWNIKA - komenda: [SYSTEM] ipv4 ".ljust(118,' ') + "#",
        "#" + " - SPRAWDZA CZY UZYTKOWNIK KORZYSTA Z PROXY - komenda: [SYSTEM] proxy ".ljust(118,' ') + "#",
        "#" + " - SPRAWDZA JAKI SYSTEM MA UZYTKOWNIK - komenda: [SYSTEM] os ".ljust(118,' ') + "#",
        "#" + " - SPRAWDZA JAKI BIOS MA UZYTKOWNIK - komenda: [SYSTEM] bios ".ljust(118,' ') + "#",
        "#" + " - SPRAWDZA JAKA NAZWE MA URZADZENIE UZYTKOWNIKA - komenda: [SYSTEM] hostname ".ljust(118,' ') + "#",
        "#" + " - WYSWIETLA POMOC DLA UZYTKOWNIKA - komenda: [SYSTEM] help ".ljust(118,' ') + "#",
        "#" + " Po wpisaniu komendy zatwierdzamy ją wciskajac enter. ".ljust(118,' ') + "#",
        "#" + "".ljust(118,' ') + "#",
        "#" + "_ WARNING ".ljust(118,'_') + "#",
        "#" + " Program dziala tylko dla systemów Windows lub Linux.".ljust(118,' ') + "#",
        "#" + " Dla systemów Linux prosimy o uruchomienie programu z sudo (w innym wypadku niektóre opcje moga byc niedostepne).".ljust(118,' ') + "#",
        "#" + "".ljust(118,'_') + "#",
        "".center(120,'#')
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
