import argparse

from uaf.cryptography.crypt import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt and decrypt sensitive data")
    parser.add_argument(
        "--mode",
        choices=["encrypt", "decrypt", "generate_key"],
        help="choose either encrypt/decrypt or generate_key as mode",
    )
    parser.add_argument("--key", help="secret key to either encrypt/decrypt sensitive file")
    parser.add_argument("--data_file", help="Data file to be encrypted/decrypted")
    args = parser.parse_args()

    if not args.mode:
        parser.error("Please provide a mode to proceed further. See help for further infomation")

    if args.mode in ["encrypt", "decrypt"]:
        if not args.data_file:
            parser.error("Please provide a file to proceed further")

    if args.mode == "encrypt":
        encrypt_file(args.data_file, args.key.encode())
    elif args.mode == "decrypt":
        decrypt_file(args.data_file, args.key.encode())
    elif args.mode == "generate_key":
        print(generate_key().decode())
