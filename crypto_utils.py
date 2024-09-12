import subprocess
import os

SERVER_PRIVATE_KEY = "keys/server_private.pem"
SERVER_PUBLIC_KEY = "keys/server_public.pem"

def generate_rsa_keys():
    os.makedirs("keys", exist_ok=True)
    if not os.path.exists(SERVER_PRIVATE_KEY) or not os.path.exists(SERVER_PUBLIC_KEY):
        subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", SERVER_PRIVATE_KEY, "-pkeyopt", "rsa_keygen_bits:2048"], check=True)
        subprocess.run(["openssl", "rsa", "-pubout", "-in", SERVER_PRIVATE_KEY, "-out", SERVER_PUBLIC_KEY], check=True)
        print("RSA keys generated.")
    else:
        print("RSA keys already exist.")

def rsa_encrypt(message, public_key_path):
    with open("message.txt", "wb") as message_file:
        message_file.write(message)
    subprocess.run(["openssl", "pkeyutl", "-encrypt", "-inkey", public_key_path, "-pubin", "-in", "message.txt", "-out", "encrypted_key.bin"], check=True)
    with open("encrypted_key.bin", "rb") as enc_file:
        encrypted_message = enc_file.read()
    os.remove("message.txt")
    os.remove("encrypted_key.bin")
    return encrypted_message


def rsa_decrypt(ciphertext, private_key_path):
    with open("encrypted_key.bin", "wb") as enc_file:
        enc_file.write(ciphertext)
    subprocess.run(["openssl", "pkeyutl", "-decrypt", "-inkey", private_key_path, "-in", "encrypted_key.bin", "-out", "decrypted_key.txt"], check=True)
    with open("decrypted_key.txt", "rb") as dec_file:
        decrypted_message = dec_file.read()
    os.remove("encrypted_key.bin")
    os.remove("decrypted_key.txt")
    return decrypted_message

def aes_encrypt(message, aes_key):
    aes_key_hex = aes_key.hex()
    with open("plaintext.txt", "wb") as message_file:
        message_file.write(message)
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-salt","-pbkdf2", "-in", "plaintext.txt", "-out", "encrypted_message.bin", "-pass", f"pass:{aes_key_hex}"], check=True)
    with open("encrypted_message.bin", "rb") as enc_file:
        encrypted_message = enc_file.read()
    os.remove("plaintext.txt")
    os.remove("encrypted_message.bin")
    return encrypted_message


def aes_decrypt(ciphertext, aes_key):
    aes_key_hex = aes_key.hex()
    with open("encrypted_message.bin", "wb") as enc_file:
        enc_file.write(ciphertext)
    subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc","-pbkdf2", "-in", "encrypted_message.bin", "-out", "decrypted_message.txt", "-pass", f"pass:{aes_key_hex}"], check=True)
    with open("decrypted_message.txt", "rb") as dec_file:
        decrypted_message = dec_file.read()
    os.remove("encrypted_message.bin")
    os.remove("decrypted_message.txt")
    
    return decrypted_message