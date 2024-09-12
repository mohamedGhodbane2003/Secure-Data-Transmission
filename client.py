import socket
from crypto_utils import rsa_encrypt, aes_encrypt, aes_decrypt
from Crypto.Random import get_random_bytes


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    aes_key = get_random_bytes(32) 
    print("AES key generated.")
    
    encrypted_aes_key = rsa_encrypt(aes_key, "keys/server_public.pem")
    client_socket.send(encrypted_aes_key)
    print("AES key sent to the server.")
    
    message = b"Hello, Server!"
    encrypted_message = aes_encrypt(message, aes_key)
    client_socket.send(encrypted_message)
    print("Encrypted message sent to the server.")

    response = client_socket.recv(1024)
    if response:
        decrypted_response = aes_decrypt(response, aes_key)
        print(f"Response received from server: {decrypted_response.decode()}")
    
    client_socket.close()
    print("Connection closed.")

client()
