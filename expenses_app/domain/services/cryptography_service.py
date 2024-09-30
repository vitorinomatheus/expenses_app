from cryptography.fernet import Fernet
from flask import current_app, g

class CryptographyService:
    def __init__(self):
        self.fernet_key = current_app.config.get('FERNET_KEY')

    def encrypt(self, decrypted_text: str):
        fernet = Fernet(self.fernet_key)
        encrypted = fernet.encrypt(decrypted_text.encode('utf-8'))
        return str(encrypted)
    
    def decrypt(self, encrypted_text: str):
        fernet = Fernet(self.fernet_key)
        decrypted = fernet.decrypt(eval(encrypted_text)).decode('utf-8')
        return str(decrypted)
    