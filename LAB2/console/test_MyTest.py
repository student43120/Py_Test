import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication, QTextEdit
from MyTest import MyTestApp

class TestMyTestApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = MyTestApp(self.app)

    def tearDown(self):
        self.window.close()

    def test_get_ipv4_info(self):
        
        with patch('socket.gethostname') as mock_gethostname, \
                patch('socket.gethostbyname') as mock_gethostbyname, \
                patch('psutil.net_if_addrs') as mock_net_if_addrs, \
                patch('socket.gethostbyaddr') as mock_gethostbyaddr:

            mock_gethostname.return_value = 'test_host'
            mock_gethostbyname.return_value = '127.0.1.1'

            mock_addr = MagicMock()
            mock_addr.family = 2 
            mock_addr.address = '127.0.1.1'

            mock_net_if_addrs.return_value = {'eth0': [mock_addr]}
            mock_gethostbyaddr.return_value = ('test_host', [], [])

            self.window.get_ipv4_info()

            text_output = self.window.text_output.toPlainText()
            self.assertIn("IP:", text_output)
            self.assertIn("Dynamiczne", text_output)

    def test_get_system_info(self):
        
        with patch('platform.platform') as mock_platform, \
                patch('platform.architecture') as mock_architecture, \
                patch('psutil.cpu_count') as mock_cpu_count, \
                patch('psutil.virtual_memory') as mock_virtual_memory:

            mock_platform.return_value = 'Test OS'
            mock_architecture.return_value = ('64bit', 'ELF')
            mock_cpu_count.return_value = 4
            mock_virtual_memory.return_value.total = 8589934592  # 8GB

            self.window.get_system_info()

            text_output = self.window.text_output.toPlainText()
            self.assertIn("Wersja SO:", text_output)
            self.assertIn("Typ Systemu:", text_output)
            self.assertIn("Rdzenie:", text_output)
            self.assertIn("RAM:", text_output)


if __name__ == '__main__':
    unittest.main()
