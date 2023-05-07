from cryptography.fernet import Fernet


def generate_key():
    """Generate a new AES-256 key"""
    key = Fernet.generate_key()
    return key


def encrypt_file(file: str, key: bytes):
    """Encrypt a given input file using AES-256 key

    Args:
        file (str): relative file path with extension
        key (_type_): AES-256 key
    """
    f = Fernet(key)
    plain_text = __read_file(file)
    cipher_text = f.encrypt(plain_text)
    __write_file(file, cipher_text)


def decrypt_file(file: str, key: bytes):
    """Decrypt a given input file using AES-256 key

    Args:
        file (str): relative file path with extension
        key (_type_): AES-256 key
    """
    f = Fernet(key)
    cipher_text = __read_file(file)
    plain_text = f.decrypt(cipher_text)
    __write_file(file, plain_text)


def __read_file(file):
    with open(file, "rb") as _file:
        return _file.read()


def __write_file(file, content):
    with open(file, "wb") as _file:
        _file.write(content)
