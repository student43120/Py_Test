import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication

from MyTest.py import MainWindow, get_ipv4, check_proxy, get_os_version, get_bios_version, get_hostname, get_help

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.exit()

    def test_get_ipv4(self):

    
        window = MainWindow()
        ipv4_button = window.findChild(QPushButton, "ipv4_button")

        ipv4_button.click()

        self.assertIn("Twój adres IPv4", window.text_view.text())

    def test_check_proxy(self):
        window = MainWindow()
        proxy_button = window.findChild(QPushButton, "proxy_button")
        with patch('subprocess.check_output', return_value=b'Direct access (no proxy server)'):
            proxy_button.click()
            self.assertIn("Nie jest uruchomione żadne proxy.", window.text_view.text())

    def test_get_os_version(self):
        window = MainWindow()
        os_button = window.findChild(QPushButton, "os_button")

        os_button.click()
        self.assertIn("Wersja systemu operacyjnego", window.text_view.text())

    def test_get_bios_version(self):
        window = MainWindow()
        bios_button = window.findChild(QPushButton, "bios_button")

        bios_button.click()
        self.assertIn("Wersja BIOS", window.text_view.text())

    def test_get_hostname(self):
        window = MainWindow()
        hostname_button = window.findChild(QPushButton, "hostname_button")

        hostname_button.click()
        self.assertIn("Host name", window.text_view.text())

    def test_get_help(self):
        window = MainWindow()
        help_button = window.findChild(QPushButton, "help_button")

        help_button.click()
        self.assertIn("MY TEST", window.text_view.text())

if __name__ == '__main__':
    unittest.main()
