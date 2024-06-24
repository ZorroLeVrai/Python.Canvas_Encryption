from file import load_data
from encryption import encrypt_file, decrypt_file

def encryption_example() -> bytes:
    key = load_data("key.txt")
    input = load_data("Pythagore_V1.png")
    return encrypt_file(key, input)


def decryption_example():
    key = load_data("key.txt")
    input = load_data("Pythagore_encrypted.png")
    return decrypt_file(key, input)

