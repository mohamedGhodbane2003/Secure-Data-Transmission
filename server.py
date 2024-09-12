import socket
from crypto_utils import generate_rsa_keys, rsa_decrypt, aes_decrypt, aes_encrypt

def server():
    generate_rsa_keys()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    encrypted_aes_key = conn.recv(256)
    aes_key = rsa_decrypt(encrypted_aes_key, "keys/server_private.pem")
    print("AES key successfully received and decrypted.")
    
    encrypted_data = conn.recv(1024)
    if encrypted_data: 
        decrypted_message = aes_decrypt(encrypted_data, aes_key) 
    
        print(f"Decrypted message: {decrypted_message.decode()}")
        response = b"Hello, Client!"
        encrypted_data = aes_encrypt(response, aes_key)
        conn.send(encrypted_data)
        print("Encrypted response sent to the client.")

    conn.close()
    print("Connection closed.")

server()
