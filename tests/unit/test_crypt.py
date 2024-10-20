import os
import tempfile
from pytest import mark, raises

from uaf.cryptic.crypt import generate_key, encrypt_file, decrypt_file


@mark.unit_test
def test_generate_key():
    key = generate_key()
    assert isinstance(key, bytes)
    assert len(key) == 44  # Base64 encoded 32-byte key


@mark.unit_test
@mark.parametrize(
    "test_message", [b"This is a test message.", b"Another test message."]
)
def test_encrypt_decrypt_file(test_message):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(test_message)
        temp_file_path = temp_file.name

    try:
        key = generate_key()

        encrypt_file(temp_file_path, key)
        with open(temp_file_path, "rb") as f:
            encrypted_content = f.read()
        assert encrypted_content != test_message

        decrypt_file(temp_file_path, key)
        with open(temp_file_path, "rb") as f:
            decrypted_content = f.read()
        assert decrypted_content == test_message

    finally:
        os.unlink(temp_file_path)


@mark.unit_test
def test_encrypt_decrypt_with_wrong_key():
    test_message = b"This is another test message."
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(test_message)
        temp_file_path = temp_file.name

    try:
        key1 = generate_key()
        key2 = generate_key()

        encrypt_file(temp_file_path, key1)

        # Use pytest.raises to expect an exception
        with raises(Exception):
            decrypt_file(temp_file_path, key2)

    finally:
        os.unlink(temp_file_path)
