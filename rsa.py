import random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit,
                             QTextEdit, QVBoxLayout, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy)
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def xgcd(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0
    while b != 0:
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
    return a, old_x, old_y

def mod_pow(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent //= 2
        base = (base * base) % mod
    return result

def choose_keys():
    with open('primes_to_100k.txt', 'r') as f:
        primes = list(map(int, f.read().splitlines()))
    filtered_primes = [p for p in primes if p >= 17]
    while True:
        p = random.choice(filtered_primes)
        q = random.choice(filtered_primes)
        if p != q:
            n = p * q
            if n >= 256:
                break
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
    _, d, _ = xgcd(e, phi)
    if d < 0:
        d += phi
    return p, q, n, phi, e, d

def encrypt_char(char, e, n):
    return mod_pow(ord(char), e, n)

def decrypt_char(cipher, d, n):
    return chr(mod_pow(cipher, d, n))

class RSAApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NETWORK SECURITY ASSIGNMENT")
        self.p, self.q, self.n, self.phi, self.e, self.d = choose_keys()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("RSA ALGORITHM")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.key_button = QPushButton("Show Key Details")
        self.key_button.clicked.connect(self.show_keys)
        layout.addWidget(self.key_button)

        layout.addWidget(QLabel("Enter message to encrypt:"))
        self.message_entry = QLineEdit()
        layout.addWidget(self.message_entry)

        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        layout.addWidget(QLabel("Encrypted message (as list of integers):"))
        self.encrypted_box = QTextEdit()
        self.encrypted_box.setReadOnly(True)
        layout.addWidget(self.encrypted_box)

        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        layout.addWidget(QLabel("Decrypted message:"))
        self.decrypted_label = QLabel("")
        self.decrypted_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.decrypted_label)

        self.setLayout(layout)

    def encrypt_message(self):
        msg = self.message_entry.text()
        if not msg:
            QMessageBox.warning(self, "Input Error", "Please enter a message to encrypt.")
            return
        self.encrypted = [encrypt_char(c, self.e, self.n) for c in msg]
        self.encrypted_box.setPlainText(str(self.encrypted))

    def decrypt_message(self):
        if not hasattr(self, 'encrypted') or not self.encrypted:
            QMessageBox.critical(self, "Decryption Error", "No encrypted message found.")
            return
        decrypted = ''.join([decrypt_char(val, self.d, self.n) for val in self.encrypted])
        self.decrypted_label.setText(decrypted)

    def show_keys(self):
        key_info = (
            f"p = {self.p}\n"
            f"q = {self.q}\n"
            f"n = {self.n}\n"
            f"phi = {self.phi}\n"
            f"e = {self.e}\n"
            f"d = {self.d}"
        )
        QMessageBox.information(self, "RSA Key Details", key_info)

if __name__ == "__main__":
    from PyQt5.QtCore import Qt
    app = QApplication(sys.argv)
    window = RSAApp()
    window.show()
    sys.exit(app.exec_())