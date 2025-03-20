from file import load_data
from encryption import encrypt_input, decrypt_input

def encryption_example() -> bytes:
    key = load_data("key.txt")
    input = load_data("Pythagore_V1.png")
    return encrypt_input(key, input)


def decryption_example():
    key = load_data("key.txt")
    input = load_data("Pythagore_encrypted.png")
    return decrypt_input(key, input)

