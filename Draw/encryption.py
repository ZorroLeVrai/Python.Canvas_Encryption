from cryptography.fernet import Fernet

def generate_encryption_key() -> bytes:
    return Fernet.generate_key()


def handle_encryption(key: bytes, input: bytes, encrypt: bool) -> bytes:
    fernet = Fernet(key)

    # encrypt or decrypt the data
    output = fernet.encrypt(input) if encrypt else fernet.decrypt(input)

    return output

def encrypt_file(key: bytes, input: bytes) -> bytes:
    return handle_encryption(key, input, True)

def decrypt_file(key: bytes, input: bytes) -> bytes:
    return handle_encryption(key, input, False)
