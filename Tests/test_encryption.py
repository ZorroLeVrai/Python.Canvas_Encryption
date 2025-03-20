import pytest
import string
from Draw import generate_encryption_key, encrypt_input, decrypt_input

@pytest.fixture
def initial_setup():
    key = generate_encryption_key()
    return key


def test_encryption_decryption(initial_setup):
    key = initial_setup
    initial_data = string.ascii_lowercase.encode("utf-8")
    processed_data = encrypt_input(key, initial_data)
    output_data = decrypt_input(key, processed_data)
    assert initial_data == output_data
