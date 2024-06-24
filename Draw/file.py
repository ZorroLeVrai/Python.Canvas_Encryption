def save_data(fileName: str, key: bytes) -> None:
    with open(fileName, 'wb') as filekey:
        filekey.write(key)

def load_data(fileName: str) -> bytes:
    with open(fileName, 'rb') as filekey:
        return filekey.read()